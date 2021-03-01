import connexion
import six
import os

from human_api.models.error_notcreate_response import ErrorNotcreateResponse  # noqa: E501
from human_api.models.error_notexist_response import ErrorNotexistResponse  # noqa: E501
from human_api.models.error_parameter_response import ErrorParameterResponse  # noqa: E501
from human_api.models.factory_create_body import FactoryCreateBody  # noqa: E501
from human_api.models.job_list_response import JobListResponse  # noqa: E501
from human_api.models.string_data_response import StringDataResponse  # noqa: E501
from human_api.util import _binary_launch_search
from hmt_escrow.eth_bridge import get_factory as eth_bridge_factory, deploy_factory, get_w3


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
        w3 = get_w3()
        try:
            factory_launch = _binary_launch_search(w3, address, 0, w3.eth.blockNumber)
            factory = eth_bridge_factory(address)
            escrows = []
            for event in factory.events.Launched.createFilter(
                    fromBlock=factory_launch).get_all_entries():
                escrows.append(event.get("args", {}).get("escrow", ""))
            return JobListResponse(escrows), 200
        except ValueError as e:
            return ErrorParameterResponse(str(e), "address"), 400
        except Exception as e:
            return ErrorNotexistResponse(str(e)), 404
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
        if body.network_id == 0:
            try:
                return StringDataResponse(
                    deploy_factory(gas_payer=body.gas_payer,
                                   gas_payer_priv=body.gas_payer_private)), 200
            except Exception as e:
                return ErrorNotcreateResponse(str(e)), 500
        else:
            return ErrorParameterResponse("This chain is not yet supported", "network_id"), 400
