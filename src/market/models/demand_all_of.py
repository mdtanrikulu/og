# coding: utf-8

"""
    Yagna Market API

     ## Yagna Market The Yagna Market is a core component of the Yagna Network, which enables computational Offers and Demands circulation. The Market is open for all entities willing to buy computations (Demands) or monetize computational resources (Offers). ## Yagna Market API The Yagna Market API is the entry to the Yagna Market through which Requestors and Providers can publish their Demands and Offers respectively, find matching counterparty, conduct negotiations and make an agreement.  This version of Market API conforms with capability level 1 of the <a href=\"https://docs.google.com/document/d/1Zny_vfgWV-hcsKS7P-Kdr3Fb0dwfl-6T_cYKVQ9mkNg\"> Market API specification</a>.  Market API contains two roles: Requestors and Providers which are symmetrical most of the time (excluding agreement phase).   # noqa: E501

    The version of the OpenAPI document: 1.5.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from src.configuration import Configuration


class DemandAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'demand_id': 'str',
        'requestor_id': 'str'
    }

    attribute_map = {
        'demand_id': 'demandId',
        'requestor_id': 'requestorId'
    }

    def __init__(self, demand_id=None, requestor_id=None, local_vars_configuration=None):  # noqa: E501
        """DemandAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._demand_id = None
        self._requestor_id = None
        self.discriminator = None

        if demand_id is not None:
            self.demand_id = demand_id
        if requestor_id is not None:
            self.requestor_id = requestor_id

    @property
    def demand_id(self):
        """Gets the demand_id of this DemandAllOf.  # noqa: E501


        :return: The demand_id of this DemandAllOf.  # noqa: E501
        :rtype: str
        """
        return self._demand_id

    @demand_id.setter
    def demand_id(self, demand_id):
        """Sets the demand_id of this DemandAllOf.


        :param demand_id: The demand_id of this DemandAllOf.  # noqa: E501
        :type demand_id: str
        """

        self._demand_id = demand_id

    @property
    def requestor_id(self):
        """Gets the requestor_id of this DemandAllOf.  # noqa: E501


        :return: The requestor_id of this DemandAllOf.  # noqa: E501
        :rtype: str
        """
        return self._requestor_id

    @requestor_id.setter
    def requestor_id(self, requestor_id):
        """Sets the requestor_id of this DemandAllOf.


        :param requestor_id: The requestor_id of this DemandAllOf.  # noqa: E501
        :type requestor_id: str
        """

        self._requestor_id = requestor_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DemandAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DemandAllOf):
            return True

        return self.to_dict() != other.to_dict()
