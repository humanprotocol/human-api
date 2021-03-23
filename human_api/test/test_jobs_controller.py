# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO
from decimal import Decimal

from human_api.models.bool_data_response import BoolDataResponse  # noqa: E501
from human_api.models.error_notcreate_response import ErrorNotcreateResponse  # noqa: E501
from human_api.models.error_notexist_response import ErrorNotexistResponse  # noqa: E501
from human_api.models.error_parameter_response import ErrorParameterResponse  # noqa: E501
from human_api.models.error_unauthorized_response import ErrorUnauthorizedResponse  # noqa: E501
from human_api.models.int_data_response import IntDataResponse  # noqa: E501
from human_api.models.job_create_body import JobCreateBody  # noqa: E501
from human_api.models.store_job_intermediate_results_body import StoreJobIntermediateResultsBody  # noqa: E501
from human_api.models.bulk_payout_job_body import BulkPayoutJobBody  # noqa: E501
from human_api.models.add_job_trusted_handlers_body import AddJobTrustedHandlersBody  # noqa: E501
from human_api.models.job_status_response import JobStatusResponse  # noqa: E501
from human_api.models.string_data_response import StringDataResponse  # noqa: E501
from human_api.test import BaseTestCase
from human_api.test.config import FACTORY_ADDRESS, GAS_PAYER, GAS_PAYER_PRIV, REP_ORACLE_PUB_KEY, RESULTS_PATH, PAYOUTS_PATH, MANIFEST_PATH
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
        job.setup()
        query_string = [('address', job.job_contract.address), ('gasPayer', GAS_PAYER),
                        ('gasPayerPrivate', GAS_PAYER_PRIV)]
        response = self.client.open('/job/abort', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))

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
                        ('gasPayerPrivate', GAS_PAYER_PRIV)]
        response = self.client.open('/job/cancel', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))

    def test_complete_job(self):
        """Test case for complete_job

        Complete a given job
        """
        with open(f"{PAYOUTS_PATH}", "r") as payouts_file:
            data = payouts_file.read()
        payouts = [(address, Decimal(amount)) for (address, amount) in json.loads(data).items()]
        job = Job({
            "gas_payer": GAS_PAYER,
            "gas_payer_priv": GAS_PAYER_PRIV
        }, manifest, FACTORY_ADDRESS)
        job.launch(REP_ORACLE_PUB_KEY)
        job.setup()
        job.bulk_payout(payouts, {}, REP_ORACLE_PUB_KEY)
        query_string = [('address', job.job_contract.address), ('gasPayer', GAS_PAYER),
                        ('gasPayerPrivate', GAS_PAYER_PRIV)]
        response = self.client.open('/job/complete', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))
        self.assertTrue(json.loads(response.data.decode('utf-8')).get("success", False))

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
                        ('gasPayerPrivate', GAS_PAYER_PRIV)]
        response = self.client.open('/job/balance', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))

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
                        ('gasPayerPrivate', GAS_PAYER_PRIV)]
        response = self.client.open('/job/launcher', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))

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
                        ('gasPayerPrivate', GAS_PAYER_PRIV)]
        response = self.client.open('/job/manifestHash', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))

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
                        ('gasPayerPrivate', GAS_PAYER_PRIV)]
        response = self.client.open('/job/manifestUrl', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))

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
                        ('gasPayerPrivate', GAS_PAYER_PRIV)]
        response = self.client.open('/job/status', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))

    def test_new_job(self):
        """Test case for new_job

        Creates a new Job and returns the address
        """
        manifest_url = f"file://{MANIFEST_PATH}"
        body = JobCreateBody(GAS_PAYER, GAS_PAYER_PRIV, FACTORY_ADDRESS,
                             REP_ORACLE_PUB_KEY.decode("utf-8"), manifest_url)
        response = self.client.open('/job',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))

    def test_store_job_intermediate_results_job(self):
        """Test case for store_job_intermediate_results_job

        Store intermediate results to S3 for the given escrow
        """
        results_url = f"file://{RESULTS_PATH}"
        job = Job({
            "gas_payer": GAS_PAYER,
            "gas_payer_priv": GAS_PAYER_PRIV
        }, manifest, FACTORY_ADDRESS)
        job.launch(REP_ORACLE_PUB_KEY)
        job.setup()
        body = StoreJobIntermediateResultsBody(GAS_PAYER, GAS_PAYER_PRIV, job.job_contract.address,
                                               REP_ORACLE_PUB_KEY.decode("utf-8"), results_url)
        response = self.client.open('/job/storeIntermediateResults',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))
        self.assertTrue(json.loads(response.data.decode('utf-8')).get("success", False))

    def test_bulk_payout_job(self):
        """Test case for bulk_payout_job

        Performs a payout to multiple ethereum addresses.
        """
        results_url = f"file://{RESULTS_PATH}"
        payouts_url = f"file://{PAYOUTS_PATH}"
        job = Job({
            "gas_payer": GAS_PAYER,
            "gas_payer_priv": GAS_PAYER_PRIV
        }, manifest, FACTORY_ADDRESS)
        job.launch(REP_ORACLE_PUB_KEY)
        job.setup()
        body = BulkPayoutJobBody(GAS_PAYER, GAS_PAYER_PRIV, job.job_contract.address,
                                 REP_ORACLE_PUB_KEY.decode("utf-8"), results_url, payouts_url)
        response = self.client.open('/job/bulkPayout',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))
        self.assertTrue(json.loads(response.data.decode('utf-8')).get("success", False))

    def test_add_job_trusted_handlers(self):
        """Test case for add_job_trusted_handlers

        Add trusted handlers that can freely transact with the contract
        """
        trusted_handlers = [
            '0x61F9F0B31eacB420553da8BCC59DC617279731Ac',
            '0xD979105297fB0eee83F7433fC09279cb5B94fFC6'
        ]
        job = Job({
            "gas_payer": GAS_PAYER,
            "gas_payer_priv": GAS_PAYER_PRIV
        }, manifest, FACTORY_ADDRESS)
        job.launch(REP_ORACLE_PUB_KEY)
        job.setup()
        body = AddJobTrustedHandlersBody(GAS_PAYER, GAS_PAYER_PRIV, job.job_contract.address,
                                         trusted_handlers)
        response = self.client.open('/job/addTrustedHandlers',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))
        self.assertTrue(json.loads(response.data.decode('utf-8')).get("success", False))

    # NOTICE: Need to fix hmt-escrow for this to work
    #
    # def test_intermediate_results_job(self):
    #     """Test case for intermediate_results_job

    #     Retrieve the intermediate results stored by the Recording Oracle
    #     """
    #     job = Job({
    #         "gas_payer": GAS_PAYER,
    #         "gas_payer_priv": GAS_PAYER_PRIV
    #     }, manifest, FACTORY_ADDRESS)
    #     job.launch(REP_ORACLE_PUB_KEY)
    #     job.setup()
    #     job.store_intermediate_results({"results": True}, REP_ORACLE_PUB_KEY)
    #     query_string = [('address', job.job_contract.address), ('gasPayer', GAS_PAYER),
    #                     ('gasPayerPrivate', GAS_PAYER_PRIV),
    #                     ('repOraclePrivate', GAS_PAYER_PRIV.lstrip("0x"))]
    #     response = self.client.open('/job/intermediateResults',
    #                                 method='GET',
    #                                 query_string=query_string)
    #     self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))

    def test_final_results_job(self):
        """Test case for final_results_job

        Retrieve the final results stored by the Recording Oracle
        """
        job = Job({
            "gas_payer": GAS_PAYER,
            "gas_payer_priv": GAS_PAYER_PRIV
        }, manifest, FACTORY_ADDRESS)
        job.launch(REP_ORACLE_PUB_KEY)
        job.setup()
        payouts = [("0x852023fbb19050B8291a335E5A83Ac9701E7B4E6", Decimal('100.0'))]
        job.bulk_payout(payouts, {'results': 0}, REP_ORACLE_PUB_KEY)
        query_string = [('address', job.job_contract.address), ('gasPayer', GAS_PAYER),
                        ('gasPayerPrivate', GAS_PAYER_PRIV),
                        ('repOraclePrivate', GAS_PAYER_PRIV.lstrip("0x"))]
        response = self.client.open('/job/finalResults', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
