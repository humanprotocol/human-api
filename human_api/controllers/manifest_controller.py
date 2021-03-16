import connexion
import six
import json

from human_api.models.error_notexist_response import ErrorNotexistResponse  # noqa: E501
from human_api.models.error_parameter_response import ErrorParameterResponse  # noqa: E501
from human_api.models.manifest_validity_response import ManifestValidityResponse  # noqa: E501
from human_api import util
from urllib.request import Request, urlopen
from basemodels import Manifest


def validate_manifest(manifest_url):  # noqa: E501
    """Validates a manifest provided by a public URL

    Validates a manifest provided by a public URL  # noqa: E501

    :param manifest_url: Publicly available manifest URL
    :type manifest_url: str

    :rtype: ManifestValidityResponse
    """
    try:
        req = Request(manifest_url)
        req.add_header(
            "User-Agent",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36"
        )
        req.add_header("X-Requested-With", "XMLHttpRequest")
        data = urlopen(req).read()
        model = json.loads(data)
    except Exception as e:
        return ErrorNotexistResponse(str(e)), 404
    try:
        Manifest(model).validate()
        return ManifestValidityResponse(True), 200
    except Exception as e:
        return ManifestValidityResponse(False, [ErrorParameterResponse(str(e), manifest_url)]), 200
