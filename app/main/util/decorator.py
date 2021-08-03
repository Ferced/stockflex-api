from functools import wraps
from http import HTTPStatus
from app.main.helpers.rate_limit import RateLimit
from flask import request
from typing import Callable


def ip_limiter(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        is_ip_allowed = RateLimit.is_ip_allowed(request)
        if not is_ip_allowed:
            response_object = {"status": "error", "message": "Too many requests"}
            status = HTTPStatus.TOO_MANY_REQUESTS
            return response_object, status
        return f(*args, **kwargs)
    return decorated

def path_limiter(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        is_path_allowed = RateLimit.is_path_allowed(request)

        if not is_path_allowed:
            response_object = {"status": "error", "message": "Too many requests"}
            status = HTTPStatus.TOO_MANY_REQUESTS
            return response_object, status

        return f(*args, **kwargs)

    return decorated
