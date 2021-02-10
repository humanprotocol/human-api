import connexion
import six

from human_api.models.network_list_response import NetworkListResponse  # noqa: E501
from human_api.models.network_stats_response import NetworkStatsResponse  # noqa: E501
from human_api import util


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
