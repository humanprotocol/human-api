import connexion
import six
import os

from human_api.models.error_notcreate_response import ErrorNotcreateResponse  # noqa: E501
from human_api.models.error_notexist_response import ErrorNotexistResponse  # noqa: E501
from human_api.models.error_parameter_response import ErrorParameterResponse  # noqa: E501
from human_api.models.factory_create_body import FactoryCreateBody  # noqa: E501
from human_api.models.job_list_response import JobListResponse  # noqa: E501
from human_api.models.string_data_response import StringDataResponse  # noqa: E501
from human_api import util
from hmt_escrow.eth_bridge import get_factory as eth_bridge_factory, deploy_factory, get_w3
from web3 import Web3
from web3.middleware import geth_poa_middleware
from solcx import compile_files


# This will find the launch block number of any contract
def _binary_launch_search(w3, address, low_b, high_b):
    """
    Pretty basic binary search: goes through all the blocks and looks for the
    block number when the given address was launched.
    """
    if not w3.isChecksumAddress(address):
        raise ValueError(
            "Invalid address provided, either not checksumed or not an actual address.")

    if high_b >= low_b:
        block = (high_b + low_b) // 2

        if w3.eth.getCode(address, block_identifier=block
                          ):  # contract has been launched before or when `block` was mined.
            # The getCode function wil retrieve the bytecode at that address (basically it tells us whether there's any contract launched at that address)
            if not w3.eth.getCode(address, block_identifier=block -
                                  1):  # contract has been launched when `block` was mined.
                return block
            else:
                return _binary_launch_search(w3, address, low_b, block - 1)
        else:
            return _binary_launch_search(w3, address, block + 1, high_b)
    else:
        raise LookupError(f"cant find contract launched at address {address} in blockchain")


def get_factory(address, gas_payer, gas_payer_private, network_key=None):  # noqa: E501
    """Returns addresses of all jobs deployed in the factory

    Receive the list of all jobs in the factory  # noqa: E501

    :param address: Deployed Factory address
    :type address: str
    :param gas_payer: address paying for the gas costs
    :type gas_payer: str
    :param gas_payer_private: Private Key for the address paying for the gas costs
    :type gas_payer_private: str
    :param network_key: Unique Identifier for the blockchain network to use. (0 is the default for Ethereum mainnet)
    :type network_key: int

    :rtype: JobListResponse
    """
    if network_key == 0:  # Ethereum Rinkeby
        try:
            HMT_ETH_SERVER = os.getenv("HMT_ETH_SERVER")
            # If connected to Rinkeby on Infura
            INFURA_PID = HMT_ETH_SERVER.split("rinkeby.infura.io/v3/", 1)[1]
            w3 = Web3(Web3.WebsocketProvider(f"wss://rinkeby.infura.io/ws/v3/{INFURA_PID}"))
        except IndexError:
            # If connected to local ganache
            GANACHE_PID = HMT_ETH_SERVER.split("http://", 1)[1]
            w3 = Web3(Web3.WebsocketProvider(f"ws://{GANACHE_PID}"))

        # Required for the Rinkeby testnet
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)

        CONTRACT_FOLDER = os.getenv("CONTRACT_FOLDER")

        CONTRACTS = compile_files([
            "{}/Escrow.sol".format(CONTRACT_FOLDER),
            "{}/EscrowFactory.sol".format(CONTRACT_FOLDER),
            "{}/HMToken.sol".format(CONTRACT_FOLDER),
            "{}/HMTokenInterface.sol".format(CONTRACT_FOLDER),
            "{}/SafeMath.sol".format(CONTRACT_FOLDER),
        ])

        contract_interface = CONTRACTS["{}/EscrowFactory.sol:EscrowFactory".format(
            CONTRACT_FOLDER)]

        try:
            factory_launch = _binary_launch_search(w3, address, 0, w3.eth.blockNumber)
            factory = w3.eth.contract(address=address, abi=contract_interface["abi"])
            escrows = []
            for event in factory.events.Launched.create_filter(
                    from_block=factory_launch).get_all_entries():
                escrows.append(event.get("args", {}).get("escrow", ""))
            return JobListResponse(escrows), 200
        except ValueError as e:
            return ErrorParameterResponse(e, "address"), 400
        except Exception as e:
            return ErrorNotexistResponse(e), 404
    else:
        # TODO: Other blockchains
        return ErrorParameterResponse("This chain is not yet supported", "network_key"), 400


def new_factory(body=None):  # noqa: E501
    """Creates a new factory and returns the address

    Creates a new factory and returns the address # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: StringDataResponse
    """
    if connexion.request.is_json:
        body = FactoryCreateBody.from_dict(connexion.request.get_json())  # noqa: E501
        if body.network_id() == 0:
            try:
                return StringDataResponse(
                    deploy_factory(gas_payer=body.gas_payer(),
                                   gas_payer_priv=body.gas_payer_private())), 200
            except Exception as e:
                return ErrorNotcreateResponse(e), 500
        else:
            return ErrorParameterResponse("This chain is not yet supported", "network_id"), 400
