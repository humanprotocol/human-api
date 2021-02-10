import hashlib
import logging
import os
import sys
import requests
import json
import urllib
import time
import hmt_escrow

from retry import retry

from typing import List, Dict, Tuple
from web3 import Web3, WebsocketProvider
from web3._utils.events import get_event_data
from web3._utils.contracts import find_matching_event_abi
from web3.middleware import geth_poa_middleware
from web3.exceptions import MismatchedABI
from hmt_escrow.job import Job, Status, launcher, manifest_url, manifest_hash, status
from hmt_escrow.eth_bridge import get_escrow

from hmt_escrow.storage import download


from chainsync.config import CONTRACT_URLS, ETH_SERVER, HMTOKEN_ADDR, GAS_PAYER, FACTORY_ADDR, EXCHANGE_URI, REQUESTER_PRIV

from contracts.interface import ContractsInterface

# Setup Logging
LOGGER = logging.getLogger("ChainSync")
logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))

def _setup_web3():
    provider = WebsocketProvider(ETH_SERVER)
    w3 = Web3(provider)
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    return w3

class Synchroniser():
    def __init__(self):
        self.w3 = _setup_web3()
        self.contracts_interface = ContractsInterface(CONTRACT_URLS)
        self.launched_api = find_matching_event_abi(self.contracts_interface.get_abi('EscrowFactory'), 'Launched', ['eip20', 'escrow'])
        self.launched_addrs = dict()
        self.factory_addr = Web3.toChecksumAddress(FACTORY_ADDR)
        self.hmtoken_addr = Web3.toChecksumAddress(HMTOKEN_ADDR)
        self.gas_payer = Web3.toChecksumAddress(GAS_PAYER)
        self.requester_priv = REQUESTER_PRIV
        self.exchange_uri = EXCHANGE_URI


    def _get_new_launched_addr(self, filter_params):
        LOGGER.info("Started Synchronisation: {}".format(filter_params))
        logs = self.w3.eth.getLogs(filter_params)
        for log in logs:
            try:
                event = get_event_data(self.w3.codec, self.launched_api, log)
                eip20_addr = event['args']['eip20']
                escrow_addr = event['args']['escrow']
                tx_hash = event['transactionHash'].hex()
                contract = self.contracts_interface.get_contract(self.w3, 'Escrow', escrow_addr)
                launcher_ = launcher(contract, self.gas_payer)
                if eip20_addr == self.hmtoken_addr:
                    if escrow_addr not in self.launched_addrs and launcher_ == self.factory_addr:
                        self.launched_addrs[escrow_addr] = tx_hash
                        LOGGER.info(f"New HMT escrow spotted at: {str(tx_hash)}")
            except Exception as e:
                LOGGER.error(f"Interrupted getting all new addresses: {e}")      
        return list(self.launched_addrs.items())


    def _add_job_to_runner(self, addr, tx_hash):
        if not addr:
            LOGGER.debug("Empty address should not instantiated.")
            return False
        LOGGER.debug(f"Address {addr} getting inserted to exchange.")

        escrow_addr = Web3.toChecksumAddress(addr)
        escrow_contract = self.contracts_interface.get_contract(self.w3, 'Escrow', addr)
        url_ = manifest_url(escrow_contract, self.gas_payer)
        hash_ = manifest_hash(escrow_contract, self.gas_payer)

        status_ = status(escrow_contract, self.gas_payer)
        LOGGER.debug(f"url: {url_}, hash: {hash_}, status: {status_}")

        if(status_ == Status.Pending and hash_ != '' and url_ != ''):
            manifest = download(url_, self.requester_priv)
            manifest_bytes = json.dumps(manifest, sort_keys=True, ensure_ascii=True)
            calculated_hash = hashlib.sha1(manifest_bytes.encode('utf-8')).hexdigest()
            if hash_ != calculated_hash:
                raise Exception(f"Hash failed to match: {hash_} to {calculated_hash}")

            payload = {
                'job_address': escrow_addr,
                'manifest_url': url_,
                'manifest_status': status_.value,
                'transaction_hash': tx_hash,
                'manifest': manifest
            }
            manifest['manifest_smart_bounty_addr'] = escrow_addr
            manifest['hmtoken_addr'] = self.hmtoken_addr
            # user_api_key = manifest["job_api_key"]
            
            res = requests.post(f"{self.exchange_uri}/escrow-job", json=payload)

            if res.status_code == 208:
                LOGGER.info(f"{escrow_addr} Job has been already consumed.")

            if not res.ok:
                # temporarily store the entire payload locally for debugging purposes
                local_filename = f'/tmp/{escrow_addr}.json'
                with open(local_filename, 'w') as fd:
                    json.dump(payload, fd)
                LOGGER.warn(f'dumped failed request to disk: {local_filename}')
                raise Exception(f"Add job failed: {res}")
            return True


    
    def run(self):
        filter_params = {'fromBlock':0, 'toBlock': 'latest', 'address': [self.factory_addr]}
        LOGGER.info("Synchronisation Server Started")
        try:
            for escrow_addr, tx_hash in self._get_new_launched_addr(filter_params):
                self._add_job_to_runner(escrow_addr, tx_hash)
        except Exception as e:
            LOGGER.error(f"Unable to synchronize: {e}")
            raise(e)
    


if __name__ == '__main__':
    synchroniser = Synchroniser()
    while True:
        try:
            synchroniser.run()
        except Exception as e:
            LOGGER.info(f"Problem synchronizing, exiting the process..")
            sys.exit(1)
        finally:
            time.sleep(15)

