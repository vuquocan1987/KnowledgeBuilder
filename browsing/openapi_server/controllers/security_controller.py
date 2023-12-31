from typing import List
from config import Config
import jwt
def info_from_BearerAuth(token):
    """
    Check and retrieve authentication information from custom bearer token.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.

    :param token Token provided by Authorization header
    :type token: str
    :return: Decoded token information or None if token is invalid
    :rtype: dict | None
    """
    try:
        uid = jwt.decode(token, Config.JWT_PUBLIC_KEY,algorithms=["RS256"])
        return {'uid': uid}
    except:
        return None

