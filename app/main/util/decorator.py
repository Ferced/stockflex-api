from functools import wraps
from app.main.helpers.limiter_helper import Limiter
from flask import request
from typing import Callable  # que es esto?


def ip_limiter(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        response_object, status = Limiter.ip_limiter(request)
        if status != 200:
            return response_object, status
        return f(*args, **kwargs)

    return decorated


def path_limiter(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        response_object, status = Limiter.path_limiter(request)

        if status != 200:
            return response_object, status

        return f(*args, **kwargs)

    return decorated


# def ip_limiter(f: Callable) -> Callable:
#     @wraps(f)
#     def decorated(*args, **kwargs):

#         data, status = Auth.get_logged_in_user(request)
#         token = data.get('data')

#         if not token:
#             return data, status

#         admin = token.get('admin')
#         if not admin:
#             response_object = {
#                 'status': 'fail',
#                 'message': 'admin token required'
#             }
#             return response_object, 401

#         return f(*args, **kwargs)

#     return decorated
