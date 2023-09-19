import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.login_post200_response import LoginPost200Response  # noqa: E501
from openapi_server.models.login_post_request import LoginPostRequest  # noqa: E501
from openapi_server.models.password_change_post_request import PasswordChangePostRequest  # noqa: E501
from openapi_server.models.password_reset_post_request import PasswordResetPostRequest  # noqa: E501
from openapi_server.models.register_post_request import RegisterPostRequest  # noqa: E501
from openapi_server import util
from openapi_server.models import user_operations


def login_post(login_post_request=None):  # noqa: E501
    """Authenticate a user

     # noqa: E501

    :param login_post_request: 
    :type login_post_request: dict | bytes

    :rtype: Union[LoginPost200Response, Tuple[LoginPost200Response, int], Tuple[LoginPost200Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        login_post_request = LoginPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
        access_token = user_operations.login(login_post_request.username, login_post_request.password)  # noqa: E501
        if access_token:
            return LoginPost200Response(access_token), 200
        else:
            return {"message": "Invalid credentials!"}, 400


def logout_post(login_post200_response=None):  # noqa: E501
    """Logout a user

     # noqa: E501

    :param login_post200_response: 
    :type login_post200_response: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        login_post200_response = LoginPost200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def password_change_post(password_change_post_request=None):  # noqa: E501
    """Change password

     # noqa: E501

    :param password_change_post_request: 
    :type password_change_post_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        password_change_post_request = PasswordChangePostRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def password_reset_post(password_reset_post_request=None):  # noqa: E501
    """Request password reset

     # noqa: E501

    :param password_reset_post_request: 
    :type password_reset_post_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        password_reset_post_request = PasswordResetPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
    
    return 'do some magic!'


def register_post(register_post_request=None):  # noqa: E501
    """Register a new user

     # noqa: E501

    :param register_post_request: 
    :type register_post_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    
    if connexion.request.is_json:
        register_post_request = RegisterPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
        registration_success = user_operations.signup(register_post_request.username, register_post_request.email, register_post_request.password)
        if registration_success:
            return None, 201
        else:
            return {"message": "User already exists!"}, 400
    else:
        return {"message": "Invalid request!"}, 400