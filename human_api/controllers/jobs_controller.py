import connexion
import six
import json

from urllib.request import Request, urlopen
from human_api.models.bool_data_response import BoolDataResponse  # noqa: E501
from human_api.models.error_notcreate_response import ErrorNotcreateResponse  # noqa: E501
from human_api.models.error_notexist_response import ErrorNotexistResponse  # noqa: E501
from human_api.models.error_parameter_response import ErrorParameterResponse  # noqa: E501
from human_api.models.error_unauthorized_response import ErrorUnauthorizedResponse  # noqa: E501
from human_api.models.int_data_response import IntDataResponse  # noqa: E501
from human_api.models.job_create_body import JobCreateBody  # noqa: E501
from human_api.models.store_job_intermediate_results_body import StoreJobIntermediateResults  # noqa: E501
from human_api.models.job_status_response import JobStatusResponse  # noqa: E501
from human_api.models.string_data_response import StringDataResponse  # noqa: E501
from human_api.util import LOGGER
from hmt_escrow.storage import download
from hmt_escrow.eth_bridge import get_escrow
from hmt_escrow.job import Job, launcher, manifest_hash, manifest_url, status
from basemodels import Manifest


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
    if network_key == 0:  # Ethereum Rinkeby
        try:
            factory_addr = launcher(get_escrow(address), gas_payer)
        except Exception as e:
            return ErrorNotexistResponse(str(e)), 404
        try:
            job = Job(credentials={
                "gas_payer": gas_payer,
                "gas_payer_priv": gas_payer_private,
                "rep_oracle_priv_key": bytes(gas_payer_private.lstrip("0x"), encoding="utf-8")
            },
                      factory_addr=factory_addr,
                      escrow_addr=address)
            return BoolDataResponse(job.abort()), 200
        except Exception as e:
            return ErrorUnauthorizedResponse(str(e)), 401
    else:
        # TODO: Other blockchains
        return ErrorParameterResponse("This chain is not yet supported", "network_key"), 400


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
    if network_key == 0:  # Ethereum Rinkeby
        try:
            factory_addr = launcher(get_escrow(address), gas_payer)
        except Exception as e:
            return ErrorNotexistResponse(str(e)), 404
        try:
            job = Job(credentials={
                "gas_payer": gas_payer,
                "gas_payer_priv": gas_payer_private,
                "rep_oracle_priv_key": bytes(gas_payer_private.lstrip("0x"), encoding="utf-8")
            },
                      factory_addr=factory_addr,
                      escrow_addr=address)
            return BoolDataResponse(job.cancel()), 200
        except Exception as e:
            return ErrorUnauthorizedResponse(str(e)), 401
    else:
        # TODO: Other blockchains
        return ErrorParameterResponse("This chain is not yet supported", "network_key"), 400


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
    if network_key == 0:  # Ethereum Rinkeby
        try:
            factory_addr = launcher(get_escrow(address), gas_payer)
        except Exception as e:
            return ErrorNotexistResponse(str(e)), 404
        try:
            job = Job(credentials={
                "gas_payer": gas_payer,
                "gas_payer_priv": gas_payer_private,
                "rep_oracle_priv_key": bytes(gas_payer_private.lstrip("0x"), encoding="utf-8")
            },
                      factory_addr=factory_addr,
                      escrow_addr=address)
            return BoolDataResponse(job.complete()), 200
        except Exception as e:
            return ErrorUnauthorizedResponse(str(e)), 401
    else:
        # TODO: Other blockchains
        return ErrorParameterResponse("This chain is not yet supported", "network_key"), 400


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
    if network_key == 0:  # Ethereum Rinkeby
        try:
            factory_addr = launcher(get_escrow(address), gas_payer)
            job = Job(credentials={
                "gas_payer": gas_payer,
                "gas_payer_priv": gas_payer_private,
                "rep_oracle_priv_key": bytes(gas_payer_private.lstrip("0x"), encoding="utf-8")
            },
                      factory_addr=factory_addr,
                      escrow_addr=address)
            return IntDataResponse(job.balance()), 200
        except Exception as e:
            return ErrorNotexistResponse(str(e)), 404
    else:
        # TODO: Other blockchains
        return ErrorParameterResponse("This chain is not yet supported", "network_key"), 400


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
    if network_key == 0:  # Ethereum Rinkeby
        try:
            return StringDataResponse(launcher(get_escrow(address), gas_payer)), 200
        except Exception as e:
            return ErrorNotexistResponse(str(e)), 404
    else:
        # TODO: Other blockchains
        return ErrorParameterResponse("This chain is not yet supported", "network_key"), 400


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
    if network_key == 0:  # Ethereum Rinkeby
        try:
            return StringDataResponse(manifest_hash(get_escrow(address), gas_payer)), 200
        except Exception as e:
            return ErrorNotexistResponse(str(e)), 404
    else:
        # TODO: Other blockchains
        return ErrorParameterResponse("This chain is not yet supported", "network_key"), 400


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
    if network_key == 0:  # Ethereum Rinkeby
        try:
            return StringDataResponse(manifest_url(get_escrow(address), gas_payer)), 200
        except Exception as e:
            return ErrorNotexistResponse(str(e)), 404
    else:
        # TODO: Other blockchains
        return ErrorParameterResponse("This chain is not yet supported", "network_key"), 400


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
    if network_key == 0:  # Ethereum Rinkeby
        try:
            return JobStatusResponse(str(status(get_escrow(address), gas_payer))), 200
        except Exception as e:
            return ErrorNotexistResponse(str(e)), 404
    else:
        # TODO: Other blockchains
        return ErrorParameterResponse("This chain is not yet supported", "network_key"), 400


def new_job(body=None):  # noqa: E501
    """Creates a new Job and returns the address

    Creates a new job and returns the address # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: StringDataResponse
    """
    if connexion.request.is_json:
        body = JobCreateBody.from_dict(connexion.request.get_json())  # noqa: E501
    if body.network_id == 0:  # Ethereum Rinkeby
        try:
            req = Request(body.manifest_url)
            req.add_header(
                "User-Agent",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36"
            )
            req.add_header("X-Requested-With", "XMLHttpRequest")
            data = urlopen(req).read()
            manifest = json.loads(data)
            job = Job({
                "gas_payer": body.gas_payer,
                "gas_payer_priv": body.gas_payer_private
            }, Manifest(manifest), body.factory_address)
        except Exception as e:
            return ErrorParameterResponse(str(e), "manifest_url or gas_payer_private"), 401
        try:
            job.launch(bytes(body.rep_oracle_pub, encoding="utf-8"))
            job.setup()
            return StringDataResponse(job.job_contract.address), 200
        except Exception as e:
            return ErrorParameterResponse(str(e), "rep_oracle_pub_key"), 401
    else:
        # TODO: Other blockchains
        return ErrorParameterResponse("This chain is not yet supported", "network_id"), 401


def store_job_interemediate_results(body=None):  # noqa: E501
    """Store intermediate results to S3 for the given escrow

    Given an escrow address, a URL where the results can be found in the form of a JSON file, and a public key will upload to S3 these intermediate results and will emit an event on the escrow contract # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: BoolDataResponse
    """
    if connexion.request.is_json:
        body = StoreJobIntermediateResults.from_dict(connexion.request.get_json())  # noqa: E501
    if body.network_id == 0:  # Ethereum Rinkeby
        try:
            factory_addr = launcher(get_escrow(body.address), body.gas_payer)
        except Exception as e:
            return ErrorNotexistResponse(str(e)), 404
        try:
            req = Request(body.results_url)
            req.add_header(
                "User-Agent",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36"
            )
            req.add_header("X-Requested-With", "XMLHttpRequest")
            data = urlopen(req).read()
            results = json.loads(data)
        except Exception as e:
            return ErrorParameterResponse(str(e), "results_url"), 400
        try:
            job = Job(credentials={
                "gas_payer": body.gas_payer,
                "gas_payer_priv": body.gas_payer_private,
                "rep_oracle_priv_key": bytes(body.gas_payer_private.lstrip("0x"), encoding="utf-8")
            },
                      factory_addr=factory_addr,
                      escrow_addr=body.address)
        except Exception as e:
            return ErrorUnauthorizedResponse(str(e)), 401
        try:
            return BoolDataResponse(
                job.store_intermediate_results(results, bytes(body.rep_oracle_pub,
                                                              encoding="utf-8"))), 200
        except Exception as e:
            return ErrorParameterResponse(str(e), "rep_oracle_pub_key"), 400
    else:
        # TODO: Other blockchains
        return ErrorParameterResponse("This chain is not yet supported", "network_id"), 400
