# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from human_api.models.error_notcreate_response import ErrorNotcreateResponse  # noqa: E501
from human_api.models.error_notexist_response import ErrorNotexistResponse  # noqa: E501
from human_api.models.error_parameter_response import ErrorParameterResponse  # noqa: E501
from human_api.models.factory_create_body import FactoryCreateBody  # noqa: E501
from human_api.models.job_list_response import JobListResponse  # noqa: E501
from human_api.models.string_data_response import StringDataResponse  # noqa: E501
from human_api.test import BaseTestCase


class TestFactoryController(BaseTestCase):
    """FactoryController integration test stubs"""
    def test_get_factory(self):
        """Test case for get_factory

        Returns addresses of all jobs deployed in the factory
        """
        query_string = [('address', 'address_example'), ('gas_payer', 'gas_payer_example'),
                        ('gas_payer_private', 'gas_payer_private_example'), ('network_key', 0)]
        response = self.client.open('/factory', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_new_factory(self):
        """Test case for new_factory

        Creates a new factory and returns the address
        """
        body = FactoryCreateBody()
        response = self.client.open('/factory',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
