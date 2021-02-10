# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.network_list_response import NetworkListResponse  # noqa: E501
from swagger_server.models.network_stats_response import NetworkStatsResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestNetworkController(BaseTestCase):
    """NetworkController integration test stubs"""

    def test_get_network_stats(self):
        """Test case for get_network_stats

        Get network statistics
        """
        query_string = [('network_id', 'network_id_example')]
        response = self.client.open(
            '/network/stats',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_networks(self):
        """Test case for get_networks

        Get list of all available networks
        """
        response = self.client.open(
            '/network',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
