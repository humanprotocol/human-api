# coding: utf-8

from __future__ import absolute_import

import os

from flask import json
from six import BytesIO

from human_api.models.error_notcreate_response import ErrorNotcreateResponse  # noqa: E501
from human_api.models.error_notexist_response import ErrorNotexistResponse  # noqa: E501
from human_api.models.error_parameter_response import ErrorParameterResponse  # noqa: E501
from human_api.models.factory_create_body import FactoryCreateBody  # noqa: E501
from human_api.models.job_list_response import JobListResponse  # noqa: E501
from human_api.models.string_data_response import StringDataResponse  # noqa: E501
from human_api.test import BaseTestCase
from hmt_escrow.eth_bridge import deploy_factory

GAS_PAYER = os.getenv("GAS_PAYER")
GAS_PAYER_PRIV = os.getenv("GAS_PAYER_PRIV")
FACTORY_ADDRESS = os.getenv("FACTORY_ADDRESS")


class TestFactoryController(BaseTestCase):
    """FactoryController integration test stubs"""
    def test_get_factory(self):
        """Test case for get_factory

        Returns addresses of all jobs deployed in the factory
        """
        query_string = [('address', FACTORY_ADDRESS), ('gasPayer', GAS_PAYER),
                        ('gasPayerPrivate', GAS_PAYER_PRIV), ('networkKey', 0)]
        response = self.client.open('/factory', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_new_factory(self):
        """Test case for new_factory

        Creates a new factory and returns the address
        """
        body = FactoryCreateBody(GAS_PAYER, GAS_PAYER_PRIV)
        response = self.client.open('/factory',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
