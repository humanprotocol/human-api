# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_notexist_response import ErrorNotexistResponse  # noqa: E501
from swagger_server.models.manifest_validity_response import ManifestValidityResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestManifestController(BaseTestCase):
    """ManifestController integration test stubs"""

    def test_validate_manifest(self):
        """Test case for validate_manifest

        Validates a manifest provided by a public URL
        """
        query_string = [('manifest_url', 'manifest_url_example')]
        response = self.client.open(
            '/manifest/validate',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
