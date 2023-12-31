from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class PasswordChangePostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, old_password=None, new_password=None, token=None):  # noqa: E501
        """PasswordChangePostRequest - a model defined in OpenAPI

        :param old_password: The old_password of this PasswordChangePostRequest.  # noqa: E501
        :type old_password: str
        :param new_password: The new_password of this PasswordChangePostRequest.  # noqa: E501
        :type new_password: str
        :param token: The token of this PasswordChangePostRequest.  # noqa: E501
        :type token: str
        """
        self.openapi_types = {
            'old_password': str,
            'new_password': str,
            'token': str
        }

        self.attribute_map = {
            'old_password': 'oldPassword',
            'new_password': 'newPassword',
            'token': 'token'
        }

        self._old_password = old_password
        self._new_password = new_password
        self._token = token

    @classmethod
    def from_dict(cls, dikt) -> 'PasswordChangePostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _password_change_post_request of this PasswordChangePostRequest.  # noqa: E501
        :rtype: PasswordChangePostRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def old_password(self) -> str:
        """Gets the old_password of this PasswordChangePostRequest.


        :return: The old_password of this PasswordChangePostRequest.
        :rtype: str
        """
        return self._old_password

    @old_password.setter
    def old_password(self, old_password: str):
        """Sets the old_password of this PasswordChangePostRequest.


        :param old_password: The old_password of this PasswordChangePostRequest.
        :type old_password: str
        """

        self._old_password = old_password

    @property
    def new_password(self) -> str:
        """Gets the new_password of this PasswordChangePostRequest.


        :return: The new_password of this PasswordChangePostRequest.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password: str):
        """Sets the new_password of this PasswordChangePostRequest.


        :param new_password: The new_password of this PasswordChangePostRequest.
        :type new_password: str
        """

        self._new_password = new_password

    @property
    def token(self) -> str:
        """Gets the token of this PasswordChangePostRequest.


        :return: The token of this PasswordChangePostRequest.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this PasswordChangePostRequest.


        :param token: The token of this PasswordChangePostRequest.
        :type token: str
        """

        self._token = token
