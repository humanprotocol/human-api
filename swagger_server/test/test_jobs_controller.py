# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.bool_data_response import BoolDataResponse  # noqa: E501
from swagger_server.models.error_notcreate_response import ErrorNotcreateResponse  # noqa: E501
from swagger_server.models.error_notexist_response import ErrorNotexistResponse  # noqa: E501
from swagger_server.models.error_parameter_response import ErrorParameterResponse  # noqa: E501
from swagger_server.models.error_unauthorized_response import ErrorUnauthorizedResponse  # noqa: E501
from swagger_server.models.int_data_response import IntDataResponse  # noqa: E501
from swagger_server.models.job_create_body import JobCreateBody  # noqa: E501
from swagger_server.models.job_status_response import JobStatusResponse  # noqa: E501
from swagger_server.models.string_data_response import StringDataResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestJobsController(BaseTestCase):
    """JobsController integration test stubs"""

    def test_abort_job(self):
        """Test case for abort_job

        Abort a given job
        """
        query_string = [('address', 'address_example'),
                        ('gas_payer', 'gas_payer_example'),
                        ('gas_payer_private', 'gas_payer_private_example'),
                        ('network_key', 0)]
        response = self.client.open(
            '/job/abort',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cancel_job(self):
        """Test case for cancel_job

        Cancel a given job
        """
        query_string = [('address', 'address_example'),
                        ('gas_payer', 'gas_payer_example'),
                        ('gas_payer_private', 'gas_payer_private_example'),
                        ('network_key', 0)]
        response = self.client.open(
            '/job/cancel',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complete_job(self):
        """Test case for complete_job

        Complete a given job
        """
        query_string = [('address', 'address_example'),
                        ('gas_payer', 'gas_payer_example'),
                        ('gas_payer_private', 'gas_payer_private_example'),
                        ('network_key', 0)]
        response = self.client.open(
            '/job/complete',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_balanace(self):
        """Test case for get_job_balanace

        Balance in HMT of a given job address
        """
        query_string = [('address', 'address_example'),
                        ('gas_payer', 'gas_payer_example'),
                        ('gas_payer_private', 'gas_payer_private_example'),
                        ('network_key', 0)]
        response = self.client.open(
            '/job/balance',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_launcher(self):
        """Test case for get_job_launcher

        Address of the launcher of a given job address
        """
        query_string = [('address', 'address_example'),
                        ('gas_payer', 'gas_payer_example'),
                        ('gas_payer_private', 'gas_payer_private_example'),
                        ('network_key', 0)]
        response = self.client.open(
            '/job/launcher',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_manifest_hash(self):
        """Test case for get_job_manifest_hash

        Manifest Hash of a given job address
        """
        query_string = [('address', 'address_example'),
                        ('gas_payer', 'gas_payer_example'),
                        ('gas_payer_private', 'gas_payer_private_example'),
                        ('network_key', 0)]
        response = self.client.open(
            '/job/manifestHash',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_manifest_url(self):
        """Test case for get_job_manifest_url

        Manifest URL of a given job address
        """
        query_string = [('address', 'address_example'),
                        ('gas_payer', 'gas_payer_example'),
                        ('gas_payer_private', 'gas_payer_private_example'),
                        ('network_key', 0)]
        response = self.client.open(
            '/job/manifestUrl',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_status(self):
        """Test case for get_job_status

        Status of a given job address
        """
        query_string = [('address', 'address_example'),
                        ('gas_payer', 'gas_payer_example'),
                        ('gas_payer_private', 'gas_payer_private_example'),
                        ('network_key', 0)]
        response = self.client.open(
            '/job/status',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_new_job(self):
        """Test case for new_job

        Creates a new Job and returns the address
        """
        body = JobCreateBody()
        response = self.client.open(
            '/job',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
