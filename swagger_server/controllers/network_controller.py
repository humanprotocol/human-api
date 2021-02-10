import connexion
import six

from swagger_server.models.network_list_response import NetworkListResponse  # noqa: E501
from swagger_server.models.network_stats_response import NetworkStatsResponse  # noqa: E501
from swagger_server import util


def get_network_stats(network_id):  # noqa: E501
    """Get network statistics

    Get network statistics  # noqa: E501

    :param network_id: Unique ID of network
    :type network_id: str

    :rtype: NetworkStatsResponse
    """
    return 'do some magic!'


def get_networks():  # noqa: E501
    """Get list of all available networks

    Get list of all available networks  # noqa: E501


    :rtype: NetworkListResponse
    """
    return 'do some magic!'
