# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from human_api.models.base_model_ import Model
from human_api import util


class AddJobTrustedHandlersBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self,
                 gas_payer: str = None,
                 gas_payer_private: str = None,
                 address: str = None,
                 handlers: List[str] = None,
                 network_id: int = 0):  # noqa: E501
        """AddJobTrustedHandlersBody - a model defined in Swagger

        :param gas_payer: The gas_payer of this AddJobTrustedHandlersBody.  # noqa: E501
        :type gas_payer: str
        :param gas_payer_private: The gas_payer_private of this AddJobTrustedHandlersBody.  # noqa: E501
        :type gas_payer_private: str
        :param address: The address of this AddJobTrustedHandlersBody.  # noqa: E501
        :type address: str
        :param handlers: The handlers of this AddJobTrustedHandlersBody.  # noqa: E501
        :type handlers: List[str]
        :param network_id: The network_id of this AddJobTrustedHandlersBody.  # noqa: E501
        :type network_id: int
        """
        self.swagger_types = {
            'gas_payer': str,
            'gas_payer_private': str,
            'address': str,
            'handlers': List[str],
            'network_id': int
        }

        self.attribute_map = {
            'gas_payer': 'gasPayer',
            'gas_payer_private': 'gasPayerPrivate',
            'address': 'address',
            'handlers': 'handlers',
            'network_id': 'networkId'
        }
        self._gas_payer = gas_payer
        self._gas_payer_private = gas_payer_private
        self._address = address
        self._handlers = handlers
        self._network_id = network_id

    @classmethod
    def from_dict(cls, dikt) -> 'AddJobTrustedHandlersBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The job_create_body of this AddJobTrustedHandlersBody.  # noqa: E501
        :rtype: AddJobTrustedHandlersBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def gas_payer(self) -> str:
        """Gets the gas_payer of this AddJobTrustedHandlersBody.


        :return: The gas_payer of this AddJobTrustedHandlersBody.
        :rtype: str
        """
        return self._gas_payer

    @gas_payer.setter
    def gas_payer(self, gas_payer: str):
        """Sets the gas_payer of this AddJobTrustedHandlersBody.


        :param gas_payer: The gas_payer of this AddJobTrustedHandlersBody.
        :type gas_payer: str
        """

        self._gas_payer = gas_payer

    @property
    def gas_payer_private(self) -> str:
        """Gets the gas_payer_private of this AddJobTrustedHandlersBody.


        :return: The gas_payer_private of this AddJobTrustedHandlersBody.
        :rtype: str
        """
        return self._gas_payer_private

    @gas_payer_private.setter
    def gas_payer_private(self, gas_payer_private: str):
        """Sets the gas_payer_private of this AddJobTrustedHandlersBody.


        :param gas_payer_private: The gas_payer_private of this AddJobTrustedHandlersBody.
        :type gas_payer_private: str
        """

        self._gas_payer_private = gas_payer_private

    @property
    def address(self) -> str:
        """Gets the address of this AddJobTrustedHandlersBody.


        :return: The address of this AddJobTrustedHandlersBody.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this AddJobTrustedHandlersBody.


        :param address: The address of this AddJobTrustedHandlersBody.
        :type address: str
        """

        self._address = address

    @property
    def handlers(self) -> List[str]:
        """Gets the handlers of this AddJobTrustedHandlersBody.


        :return: The handlers of this AddJobTrustedHandlersBody.
        :rtype: List[str]
        """
        return self._handlers

    @handlers.setter
    def handlers(self, handlers: List[str]):
        """Sets the handlers of this AddJobTrustedHandlersBody.


        :param handlers: The handlers of this AddJobTrustedHandlersBody.
        :type handlers: str
        """

        self._handlers = handlers

    @property
    def network_id(self) -> int:
        """Gets the network_id of this AddJobTrustedHandlersBody.


        :return: The network_id of this AddJobTrustedHandlersBody.
        :rtype: int
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id: int):
        """Sets the network_id of this AddJobTrustedHandlersBody.


        :param network_id: The network_id of this AddJobTrustedHandlersBody.
        :type network_id: int
        """

        self._network_id = network_id