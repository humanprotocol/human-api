# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO
from decimal import Decimal

from human_api.test import BaseTestCase
from human_api.test.config import FACTORY_ADDRESS, GAS_PAYER, GAS_PAYER_PRIV, REP_ORACLE_PUB_KEY, RESULTS_PATH, PAYOUTS_PATH
from human_api.models.factory_create_body import FactoryCreateBody
from human_api.models.job_create_body import JobCreateBody
from human_api.models.store_job_intermediate_results_body import StoreJobIntermediateResultsBody
from human_api.models.bulk_payout_job_body import BulkPayoutJobBody
from human_api.test.helpers import test_model


class TestIntegration(BaseTestCase):
    """Overall Integration tests"""
    def test_factory_creation_and_job_completion(self):
        """Test case for a complete escrow pipeline

        Create a factory, then an escrow, and complete the job.
        """
        # Create the factory
        body = FactoryCreateBody(GAS_PAYER, GAS_PAYER_PRIV)
        response = self.client.open('/factory',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))
        factory_addr = json.loads(response.data.decode('utf-8')).get("data", "")

        #  Create the job
        MANIFEST_PATH = "/work/human_api/test/dumps/test_manifest_file"
        with open(f"{MANIFEST_PATH}", "w") as test_manifest_file:
            test_manifest_file.write(json.dumps(test_model()))
        manifest_url = f"file://{MANIFEST_PATH}"
        body = JobCreateBody(GAS_PAYER, GAS_PAYER_PRIV, factory_addr,
                             REP_ORACLE_PUB_KEY.decode("utf-8"), manifest_url)
        response = self.client.open('/job',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))
        escrow_addr = json.loads(response.data.decode('utf-8')).get("data", "")

        # Store intermediate results
        results_url = f"file://{RESULTS_PATH}"
        body = StoreJobIntermediateResultsBody(GAS_PAYER, GAS_PAYER_PRIV, escrow_addr,
                                               REP_ORACLE_PUB_KEY.decode("utf-8"), results_url)
        response = self.client.open('/job/storeIntermediateResults',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))
        self.assertTrue(json.loads(response.data.decode('utf-8')).get("success", False))

        # Bulk payout
        results_url = f"file://{RESULTS_PATH}"
        payouts_url = f"file://{PAYOUTS_PATH}"
        body = BulkPayoutJobBody(GAS_PAYER, GAS_PAYER_PRIV, escrow_addr,
                                 REP_ORACLE_PUB_KEY.decode("utf-8"), results_url, payouts_url)
        response = self.client.open('/job/bulkPayout',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))
        self.assertTrue(json.loads(response.data.decode('utf-8')).get("success", False))

        # Complete job
        query_string = [('address', escrow_addr), ('gasPayer', GAS_PAYER),
                        ('gasPayerPrivate', GAS_PAYER_PRIV)]
        response = self.client.open('/job/complete', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))
        self.assertTrue(json.loads(response.data.decode('utf-8')).get("success", False))

        # Trying to cancel after completion is futile
        query_string = [('address', escrow_addr), ('gasPayer', GAS_PAYER),
                        ('gasPayerPrivate', GAS_PAYER_PRIV)]
        response = self.client.open('/job/cancel', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))
        self.assertFalse(json.loads(response.data.decode('utf-8')).get("success", True))

        # Trying to abort after completion is futile
        response = self.client.open('/job/abort', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))
        self.assertFalse(json.loads(response.data.decode('utf-8')).get("success", True))


if __name__ == '__main__':
    import unittest
    unittest.main()
