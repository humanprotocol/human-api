import os
import logging
import json
from solcx import compile_standard
from eth_typing import ChecksumAddress, HexAddress, HexStr

from contracts.downloader import download_multiple_files
# Setup Logging
LOGGER = logging.getLogger("Contracts:Interface")
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


class ContractsInterface():
    """
    Class that provides interface to compiled contracts
    """
    def __init__(self, urls, output_filename='contracts.json'):
        self._compiled_contracts = dict()
        self._urls = urls
        self._output_file_path = os.path.join(os.getcwd(), '.cache', output_filename)

        self._initialise()

    def _initialise(self):
        """
        Compiles the contracts or reads from file if cache exists
        """
        if (os.path.exists(self._output_file_path)):
            LOGGER.info("Contracts Cache exits, reading from that.")
            with open(self._output_file_path) as f:
                self._compiled_contracts = json.load(f)
            LOGGER.info("Contracts Loaded")

        else:
            LOGGER.info("Downloading Contracts from URLs")
            cache_path = os.path.split(self._output_file_path)[0]
            contracts_source = download_multiple_files(self._urls)
            solc_compile_source = dict()
            for contract in contracts_source:
                solc_compile_source[contract['filename']] = {"content": contract['content']}
            solc_compile_input = {
                "language": "Solidity",
                "sources": solc_compile_source,
                "settings": {
                    "outputSelection": {
                        "*": {
                            "*": ['*']
                        }
                    }
                }
            }
            self._compiled_contracts = compile_standard(solc_compile_input)
            # Make Cache directory
            os.mkdir(cache_path)
            with open(self._output_file_path, 'w+') as f:
                f.write(json.dumps(self._compiled_contracts))

    def get_interface(self, contract_name):
        return self._compiled_contracts['contracts']['{}.sol'.format(contract_name)][contract_name]

    def get_abi(self, contract_name):
        return self._compiled_contracts['contracts']['{}.sol'.format(
            contract_name)][contract_name]['abi']

    def get_bytecode(self, contract_name):
        return self._compiled_contracts['contracts']['{}.sol'.format(
            contract_name)][contract_name]['evm']['bytecode']['object']

    def get_contract(self, w3, contract_name, addr):
        return w3.eth.contract(
            address=ChecksumAddress(HexAddress(HexStr(addr))),
            abi=self.get_abi(contract_name),
        )
