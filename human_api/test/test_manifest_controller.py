# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from human_api.models.error_notexist_response import ErrorNotexistResponse  # noqa: E501
from human_api.models.manifest_validity_response import ManifestValidityResponse  # noqa: E501
from human_api.test import BaseTestCase
from human_api.test.config import MANIFEST_PATH, PAYOUTS_PATH


class TestManifestController(BaseTestCase):
    """ManifestController integration test stubs"""
    def test_validate_manifest(self):
        """Test case for validate_manifest

        Validates a manifest provided by a public URL
        """
        # This should be succesfully validated
        manifest_url = f"file://{MANIFEST_PATH}"
        query_string = [('manifestUrl', manifest_url)]
        response = self.client.open('/manifest/validate', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))
        self.assertTrue(json.loads(response.data.decode('utf-8')).get("valid", False))

        # The payouts data is not a valid manifest
        manifest_url = f"file://{PAYOUTS_PATH}"
        query_string = [('manifestUrl', manifest_url)]
        response = self.client.open('/manifest/validate', method='GET', query_string=query_string)
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))
        self.assertFalse(json.loads(response.data.decode('utf-8')).get("valid", True))


if __name__ == '__main__':
    import unittest
    unittest.main()
