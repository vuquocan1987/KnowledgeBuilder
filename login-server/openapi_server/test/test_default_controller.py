import unittest

from flask import json

from openapi_server.models.login_post200_response import LoginPost200Response  # noqa: E501
from openapi_server.models.login_post_request import LoginPostRequest  # noqa: E501
from openapi_server.models.password_change_post_request import PasswordChangePostRequest  # noqa: E501
from openapi_server.models.password_reset_post_request import PasswordResetPostRequest  # noqa: E501
from openapi_server.models.register_post_request import RegisterPostRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_login_post(self):
        """Test case for login_post

        Authenticate a user
        """
        login_post_request = openapi_server.LoginPostRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/login',
            method='POST',
            headers=headers,
            data=json.dumps(login_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_logout_post(self):
        """Test case for logout_post

        Logout a user
        """
        login_post200_response = openapi_server.LoginPost200Response()
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/logout',
            method='POST',
            headers=headers,
            data=json.dumps(login_post200_response),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_password_change_post(self):
        """Test case for password_change_post

        Change password
        """
        password_change_post_request = openapi_server.PasswordChangePostRequest()
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/password-change',
            method='POST',
            headers=headers,
            data=json.dumps(password_change_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_password_reset_post(self):
        """Test case for password_reset_post

        Request password reset
        """
        password_reset_post_request = openapi_server.PasswordResetPostRequest()
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/password-reset',
            method='POST',
            headers=headers,
            data=json.dumps(password_reset_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_register_post(self):
        """Test case for register_post

        Register a new user
        """
        register_post_request = openapi_server.RegisterPostRequest()
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/register',
            method='POST',
            headers=headers,
            data=json.dumps(register_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
