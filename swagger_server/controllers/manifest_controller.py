import connexion
import six

from swagger_server.models.error_notexist_response import ErrorNotexistResponse  # noqa: E501
from swagger_server.models.manifest_validity_response import ManifestValidityResponse  # noqa: E501
from swagger_server import util


def validate_manifest(manifest_url):  # noqa: E501
    """Validates a manifest provided by a public URL

    Validates a manifest provided by a public URL  # noqa: E501

    :param manifest_url: Publicly available manifest URL
    :type manifest_url: str

    :rtype: ManifestValidityResponse
    """
    return 'do some magic!'
