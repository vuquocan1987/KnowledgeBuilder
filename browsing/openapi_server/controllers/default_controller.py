import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.question import Question  # noqa: E501
from openapi_server import util


def questions_get(token_info):  # noqa: E501
    """Get list of questions

    Retrieve a list of questions available to the authenticated user. # noqa: E501

    
    :rtype: Union[List[Question], Tuple[List[Question], int], Tuple[List[Question], int, Dict[str, str]]
    """
    if token_info:
        return ["some question content"]
    
    
