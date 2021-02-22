# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from human_api.models.bool_data_response import BoolDataResponse  # noqa: E501
from human_api.models.error_notcreate_response import ErrorNotcreateResponse  # noqa: E501
from human_api.models.error_notexist_response import ErrorNotexistResponse  # noqa: E501
from human_api.models.error_parameter_response import ErrorParameterResponse  # noqa: E501
from human_api.models.error_unauthorized_response import ErrorUnauthorizedResponse  # noqa: E501
from human_api.models.int_data_response import IntDataResponse  # noqa: E501
from human_api.models.job_create_body import JobCreateBody  # noqa: E501
from human_api.models.job_status_response import JobStatusResponse  # noqa: E501
from human_api.models.string_data_response import StringDataResponse  # noqa: E501
from human_api.test import BaseTestCase
from human_api.test.config import FACTORY_ADDRESS, GAS_PAYER, GAS_PAYER_PRIV, REP_ORACLE_PUB_KEY
from human_api.test.helpers import test_model
from hmt_escrow.test_manifest import manifest
from hmt_escrow.job import Job, manifest_url


class TestJobsController(BaseTestCase):
    """JobsController integration test stubs"""
    def test_abort_job(self):
        """Test case for abort_job

        Abort a given job
        """
        job = Job({
            "gas_payer": GAS_PAYER,
            "gas_payer_priv": GAS_PAYER_PRIV
        }, manifest, FACTORY_ADDRESS)
        job.launch(REP_ORACLE_PUB_KEY)
        query_string = [('address', job.job_contract.address), ('gasPayer', GAS_PAYER),
                        ('gasPayerPrivate', GAS_PAYER_PRIV), ('networkKey', 0)]
        response = self.client.open('/job/abort', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_cancel_job(self):
        """Test case for cancel_job

        Cancel a given job
        """
        job = Job({
            "gas_payer": GAS_PAYER,
            "gas_payer_priv": GAS_PAYER_PRIV
        }, manifest, FACTORY_ADDRESS)
        job.launch(REP_ORACLE_PUB_KEY)
        job.setup()
        query_string = [('address', job.job_contract.address), ('gasPayer', GAS_PAYER),
                        ('gasPayerPrivate', GAS_PAYER_PRIV), ('networkKey', 0)]
        response = self.client.open('/job/cancel', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

    # In order to test the following, need to add the bulkPayout and store intermediate results functionalities to the API spec
    # def test_complete_job(self):
    #     """Test case for complete_job

    #     Complete a given job
    #     """
    #     query_string = [('address', 'address_example'), ('gas_payer', 'gas_payer_example'),
    #                     ('gas_payer_private', 'gas_payer_private_example'), ('network_key', 0)]
    #     response = self.client.open('/job/complete', method='GET', query_string=query_string)
    #     self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_balanace(self):
        """Test case for get_job_balanace

        Balance in HMT of a given job address
        """
        job = Job({
            "gas_payer": GAS_PAYER,
            "gas_payer_priv": GAS_PAYER_PRIV
        }, manifest, FACTORY_ADDRESS)
        job.launch(REP_ORACLE_PUB_KEY)
        job.setup()
        query_string = [('address', job.job_contract.address), ('gasPayer', GAS_PAYER),
                        ('gasPayerPrivate', GAS_PAYER_PRIV), ('networkKey', 0)]
        response = self.client.open('/job/balance', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_launcher(self):
        """Test case for get_job_launcher

        Address of the launcher of a given job address
        """
        job = Job({
            "gas_payer": GAS_PAYER,
            "gas_payer_priv": GAS_PAYER_PRIV
        }, manifest, FACTORY_ADDRESS)
        job.launch(REP_ORACLE_PUB_KEY)
        query_string = [('address', job.job_contract.address), ('gasPayer', GAS_PAYER),
                        ('gasPayerPrivate', GAS_PAYER_PRIV), ('networkKey', 0)]
        response = self.client.open('/job/launcher', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_manifest_hash(self):
        """Test case for get_job_manifest_hash

        Manifest Hash of a given job address
        """
        job = Job({
            "gas_payer": GAS_PAYER,
            "gas_payer_priv": GAS_PAYER_PRIV
        }, manifest, FACTORY_ADDRESS)
        job.launch(REP_ORACLE_PUB_KEY)
        query_string = [('address', job.job_contract.address), ('gasPayer', GAS_PAYER),
                        ('gasPayerPrivate', GAS_PAYER_PRIV), ('networkKey', 0)]
        response = self.client.open('/job/manifestHash', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_manifest_url(self):
        """Test case for get_job_manifest_url

        Manifest URL of a given job address
        """
        job = Job({
            "gas_payer": GAS_PAYER,
            "gas_payer_priv": GAS_PAYER_PRIV
        }, manifest, FACTORY_ADDRESS)
        job.launch(REP_ORACLE_PUB_KEY)
        query_string = [('address', job.job_contract.address), ('gasPayer', GAS_PAYER),
                        ('gasPayerPrivate', GAS_PAYER_PRIV), ('networkKey', 0)]
        response = self.client.open('/job/manifestUrl', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_status(self):
        """Test case for get_job_status

        Status of a given job address
        """
        job = Job({
            "gas_payer": GAS_PAYER,
            "gas_payer_priv": GAS_PAYER_PRIV
        }, manifest, FACTORY_ADDRESS)
        job.launch(REP_ORACLE_PUB_KEY)
        query_string = [('address', job.job_contract.address), ('gasPayer', GAS_PAYER),
                        ('gasPayerPrivate', GAS_PAYER_PRIV), ('networkKey', 0)]
        response = self.client.open('/job/status', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_new_job(self):
        """Test case for new_job

        Creates a new Job and returns the address
        """
        MANIFEST_PATH = "/work/human_api/test/dumps/test_manifest_file"
        with open(f"{MANIFEST_PATH}", "w") as test_manifest_file:
            test_manifest_file.write(json.dumps(test_model()))
        manifest_url = f"file://{MANIFEST_PATH}"
        body = JobCreateBody(GAS_PAYER, GAS_PAYER_PRIV, FACTORY_ADDRESS,
                             REP_ORACLE_PUB_KEY.decode("utf-8"), manifest_url)
        response = self.client.open('/job',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
