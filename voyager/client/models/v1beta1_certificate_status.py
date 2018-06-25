# coding: utf-8

"""
    Voyager

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v7.1.1
    Contact: hello@appscode.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1CertificateStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'acme_user_secret_name': 'str',
        'certificate_obtained': 'bool',
        'conditions': 'list[V1beta1CertificateCondition]',
        'creation_time': 'datetime',
        'details': 'V1beta1ACMECertificateDetails',
        'last_issued_certificate': 'V1beta1CertificateDetails',
        'message': 'str'
    }

    attribute_map = {
        'acme_user_secret_name': 'acmeUserSecretName',
        'certificate_obtained': 'certificateObtained',
        'conditions': 'conditions',
        'creation_time': 'creationTime',
        'details': 'details',
        'last_issued_certificate': 'lastIssuedCertificate',
        'message': 'message'
    }

    def __init__(self, acme_user_secret_name=None, certificate_obtained=None, conditions=None, creation_time=None, details=None, last_issued_certificate=None, message=None):
        """
        V1beta1CertificateStatus - a model defined in Swagger
        """

        self._acme_user_secret_name = None
        self._certificate_obtained = None
        self._conditions = None
        self._creation_time = None
        self._details = None
        self._last_issued_certificate = None
        self._message = None
        self.discriminator = None

        if acme_user_secret_name is not None:
          self.acme_user_secret_name = acme_user_secret_name
        if certificate_obtained is not None:
          self.certificate_obtained = certificate_obtained
        if conditions is not None:
          self.conditions = conditions
        if creation_time is not None:
          self.creation_time = creation_time
        if details is not None:
          self.details = details
        if last_issued_certificate is not None:
          self.last_issued_certificate = last_issued_certificate
        if message is not None:
          self.message = message

    @property
    def acme_user_secret_name(self):
        """
        Gets the acme_user_secret_name of this V1beta1CertificateStatus.
        Deprecated

        :return: The acme_user_secret_name of this V1beta1CertificateStatus.
        :rtype: str
        """
        return self._acme_user_secret_name

    @acme_user_secret_name.setter
    def acme_user_secret_name(self, acme_user_secret_name):
        """
        Sets the acme_user_secret_name of this V1beta1CertificateStatus.
        Deprecated

        :param acme_user_secret_name: The acme_user_secret_name of this V1beta1CertificateStatus.
        :type: str
        """

        self._acme_user_secret_name = acme_user_secret_name

    @property
    def certificate_obtained(self):
        """
        Gets the certificate_obtained of this V1beta1CertificateStatus.
        Deprecated

        :return: The certificate_obtained of this V1beta1CertificateStatus.
        :rtype: bool
        """
        return self._certificate_obtained

    @certificate_obtained.setter
    def certificate_obtained(self, certificate_obtained):
        """
        Sets the certificate_obtained of this V1beta1CertificateStatus.
        Deprecated

        :param certificate_obtained: The certificate_obtained of this V1beta1CertificateStatus.
        :type: bool
        """

        self._certificate_obtained = certificate_obtained

    @property
    def conditions(self):
        """
        Gets the conditions of this V1beta1CertificateStatus.

        :return: The conditions of this V1beta1CertificateStatus.
        :rtype: list[V1beta1CertificateCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this V1beta1CertificateStatus.

        :param conditions: The conditions of this V1beta1CertificateStatus.
        :type: list[V1beta1CertificateCondition]
        """

        self._conditions = conditions

    @property
    def creation_time(self):
        """
        Gets the creation_time of this V1beta1CertificateStatus.

        :return: The creation_time of this V1beta1CertificateStatus.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this V1beta1CertificateStatus.

        :param creation_time: The creation_time of this V1beta1CertificateStatus.
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def details(self):
        """
        Gets the details of this V1beta1CertificateStatus.
        Deprecated

        :return: The details of this V1beta1CertificateStatus.
        :rtype: V1beta1ACMECertificateDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this V1beta1CertificateStatus.
        Deprecated

        :param details: The details of this V1beta1CertificateStatus.
        :type: V1beta1ACMECertificateDetails
        """

        self._details = details

    @property
    def last_issued_certificate(self):
        """
        Gets the last_issued_certificate of this V1beta1CertificateStatus.

        :return: The last_issued_certificate of this V1beta1CertificateStatus.
        :rtype: V1beta1CertificateDetails
        """
        return self._last_issued_certificate

    @last_issued_certificate.setter
    def last_issued_certificate(self, last_issued_certificate):
        """
        Sets the last_issued_certificate of this V1beta1CertificateStatus.

        :param last_issued_certificate: The last_issued_certificate of this V1beta1CertificateStatus.
        :type: V1beta1CertificateDetails
        """

        self._last_issued_certificate = last_issued_certificate

    @property
    def message(self):
        """
        Gets the message of this V1beta1CertificateStatus.
        Deprecated

        :return: The message of this V1beta1CertificateStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this V1beta1CertificateStatus.
        Deprecated

        :param message: The message of this V1beta1CertificateStatus.
        :type: str
        """

        self._message = message

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1beta1CertificateStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
