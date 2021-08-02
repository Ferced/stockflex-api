from functools import wraps
from app.main.helpers.limiter_helper import Limiter
from flask import request
from typing import Callable

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

