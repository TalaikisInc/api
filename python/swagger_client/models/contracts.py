# coding: utf-8

"""
    PostgREST API

    standard public schema  # noqa: E501

    OpenAPI spec version: 0.5.0.0 (d8896be)
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Contracts(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'addr': 'str',
        'bytecode': 'str',
        'balance': 'float'
    }

    attribute_map = {
        'addr': 'addr',
        'bytecode': 'bytecode',
        'balance': 'balance'
    }

    def __init__(self, addr=None, bytecode=None, balance=None):  # noqa: E501
        """Contracts - a model defined in Swagger"""  # noqa: E501

        self._addr = None
        self._bytecode = None
        self._balance = None
        self.discriminator = None

        if addr is not None:
            self.addr = addr
        if bytecode is not None:
            self.bytecode = bytecode
        if balance is not None:
            self.balance = balance

    @property
    def addr(self):
        """Gets the addr of this Contracts.  # noqa: E501

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :return: The addr of this Contracts.  # noqa: E501
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this Contracts.

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :param addr: The addr of this Contracts.  # noqa: E501
        :type: str
        """
        if addr is not None and len(addr) > 42:
            raise ValueError("Invalid value for `addr`, length must be less than or equal to `42`")  # noqa: E501

        self._addr = addr

    @property
    def bytecode(self):
        """Gets the bytecode of this Contracts.  # noqa: E501


        :return: The bytecode of this Contracts.  # noqa: E501
        :rtype: str
        """
        return self._bytecode

    @bytecode.setter
    def bytecode(self, bytecode):
        """Sets the bytecode of this Contracts.


        :param bytecode: The bytecode of this Contracts.  # noqa: E501
        :type: str
        """

        self._bytecode = bytecode

    @property
    def balance(self):
        """Gets the balance of this Contracts.  # noqa: E501


        :return: The balance of this Contracts.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Contracts.


        :param balance: The balance of this Contracts.  # noqa: E501
        :type: float
        """

        self._balance = balance

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, Contracts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
