import connexion
import six

from swagger_server.models.bool_data_response import BoolDataResponse  # noqa: E501
from swagger_server.models.error_notcreate_response import ErrorNotcreateResponse  # noqa: E501
from swagger_server.models.error_notexist_response import ErrorNotexistResponse  # noqa: E501
from swagger_server.models.error_parameter_response import ErrorParameterResponse  # noqa: E501
from swagger_server.models.error_unauthorized_response import ErrorUnauthorizedResponse  # noqa: E501
from swagger_server.models.int_data_response import IntDataResponse  # noqa: E501
from swagger_server.models.job_create_body import JobCreateBody  # noqa: E501
from swagger_server.models.job_status_response import JobStatusResponse  # noqa: E501
from swagger_server.models.string_data_response import StringDataResponse  # noqa: E501
from swagger_server import util


def abort_job(address, gas_payer, gas_payer_private, network_key=None):  # noqa: E501
    """Abort a given job

    Abort a given job  # noqa: E501

    :param address: Deployed Job address
    :type address: str
    :param gas_payer: address paying which started the job or a trusted handler
    :type gas_payer: str
    :param gas_payer_private: Private Key for the address paying for the gas costs
    :type gas_payer_private: str
    :param network_key: Unique Identifier for the blockchain network to use. (0 is the default for Ethereum mainnet)
    :type network_key: int

    :rtype: BoolDataResponse
    """
    return 'do some magic!'


def cancel_job(address, gas_payer, gas_payer_private, network_key=None):  # noqa: E501
    """Cancel a given job

    Cancel a given job  # noqa: E501

    :param address: Deployed Job address
    :type address: str
    :param gas_payer: address paying which started the job or a trusted handler
    :type gas_payer: str
    :param gas_payer_private: Private Key for the address paying for the gas costs
    :type gas_payer_private: str
    :param network_key: Unique Identifier for the blockchain network to use. (0 is the default for Ethereum mainnet)
    :type network_key: int

    :rtype: BoolDataResponse
    """
    return 'do some magic!'


def complete_job(address, gas_payer, gas_payer_private, network_key=None):  # noqa: E501
    """Complete a given job

    Complete a given job  # noqa: E501

    :param address: Deployed Job address
    :type address: str
    :param gas_payer: address paying which started the job or a trusted handler
    :type gas_payer: str
    :param gas_payer_private: Private Key for the address paying for the gas costs
    :type gas_payer_private: str
    :param network_key: Unique Identifier for the blockchain network to use. (0 is the default for Ethereum mainnet)
    :type network_key: int

    :rtype: BoolDataResponse
    """
    return 'do some magic!'


def get_job_balanace(address, gas_payer, gas_payer_private, network_key=None):  # noqa: E501
    """Balance in HMT of a given job address

    Balance in HMT of a given job address  # noqa: E501

    :param address: Deployed Job address
    :type address: str
    :param gas_payer: address paying for the gas costs
    :type gas_payer: str
    :param gas_payer_private: Private Key for the address paying for the gas costs
    :type gas_payer_private: str
    :param network_key: Unique Identifier for the blockchain network to use. (0 is the default for Ethereum mainnet)
    :type network_key: int

    :rtype: IntDataResponse
    """
    return 'do some magic!'


def get_job_launcher(address, gas_payer, gas_payer_private, network_key=None):  # noqa: E501
    """Address of the launcher of a given job address

    Receive the address of the launcher of a given job address  # noqa: E501

    :param address: Deployed Job address
    :type address: str
    :param gas_payer: address paying for the gas costs
    :type gas_payer: str
    :param gas_payer_private: Private Key for the address paying for the gas costs
    :type gas_payer_private: str
    :param network_key: Unique Identifier for the blockchain network to use. (0 is the default for Ethereum mainnet)
    :type network_key: int

    :rtype: StringDataResponse
    """
    return 'do some magic!'


def get_job_manifest_hash(address, gas_payer, gas_payer_private, network_key=None):  # noqa: E501
    """Manifest Hash of a given job address

    Receive the Manifest Hash of a given job address  # noqa: E501

    :param address: Deployed Job address
    :type address: str
    :param gas_payer: address paying for the gas costs
    :type gas_payer: str
    :param gas_payer_private: Private Key for the address paying for the gas costs
    :type gas_payer_private: str
    :param network_key: Unique Identifier for the blockchain network to use. (0 is the default for Ethereum mainnet)
    :type network_key: int

    :rtype: StringDataResponse
    """
    return 'do some magic!'


def get_job_manifest_url(address, gas_payer, gas_payer_private, network_key=None):  # noqa: E501
    """Manifest URL of a given job address

    Receive the Manifest URL of a given job address  # noqa: E501

    :param address: Deployed Job address
    :type address: str
    :param gas_payer: address paying for the gas costs
    :type gas_payer: str
    :param gas_payer_private: Private Key for the address paying for the gas costs
    :type gas_payer_private: str
    :param network_key: Unique Identifier for the blockchain network to use. (0 is the default for Ethereum mainnet)
    :type network_key: int

    :rtype: StringDataResponse
    """
    return 'do some magic!'


def get_job_status(address, gas_payer, gas_payer_private, network_key=None):  # noqa: E501
    """Status of a given job address

    Receive the status of a given job address  # noqa: E501

    :param address: Deployed Job address
    :type address: str
    :param gas_payer: address paying for the gas costs
    :type gas_payer: str
    :param gas_payer_private: Private Key for the address paying for the gas costs
    :type gas_payer_private: str
    :param network_key: Unique Identifier for the blockchain network to use. (0 is the default for Ethereum mainnet)
    :type network_key: int

    :rtype: JobStatusResponse
    """
    return 'do some magic!'


def new_job(body=None):  # noqa: E501
    """Creates a new Job and returns the address

    Creates a new job and returns the address # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: StringDataResponse
    """
    if connexion.request.is_json:
        body = JobCreateBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
