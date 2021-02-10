import connexion
import six

from swagger_server.models.error_notcreate_response import ErrorNotcreateResponse  # noqa: E501
from swagger_server.models.error_notexist_response import ErrorNotexistResponse  # noqa: E501
from swagger_server.models.error_parameter_response import ErrorParameterResponse  # noqa: E501
from swagger_server.models.factory_create_body import FactoryCreateBody  # noqa: E501
from swagger_server.models.job_list_response import JobListResponse  # noqa: E501
from swagger_server.models.string_data_response import StringDataResponse  # noqa: E501
from swagger_server import util


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
    return 'do some magic!'


def new_factory(body=None):  # noqa: E501
    """Creates a new factory and returns the address

    Creates a new factory and returns the address # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: StringDataResponse
    """
    if connexion.request.is_json:
        body = FactoryCreateBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
