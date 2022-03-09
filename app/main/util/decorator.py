from __future__ import print_function
from functools import wraps
from http import HTTPStatus
from app.main.helpers.rate_limit import RateLimit
from app.main.helpers.auth_helper import Auth
from flask import request
from typing import Callable


def ip_limiter(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        is_ip_allowed = RateLimit.is_ip_allowed(request.remote_addr)

        if not is_ip_allowed:
            response_object = {"status": "error", "message": "Too many requests"}
            status = HTTPStatus.TOO_MANY_REQUESTS
            return response_object, status
        return f(*args, **kwargs)

    return decorated


def path_limiter(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        is_path_allowed = RateLimit.is_path_allowed(request.path)

        if not is_path_allowed:
            response_object = {"status": "error", "message": "Too many requests"}
            status = HTTPStatus.TOO_MANY_REQUESTS
            return response_object, status

        return f(*args, **kwargs)

    return decorated


def ip_path_combo_limiter(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        is_combo_allowed = RateLimit.is_combo_allowed(request.remote_addr, request.path)

        if not is_combo_allowed:
            response_object = {"status": "error", "message": "Too many requests"}
            status = HTTPStatus.TOO_MANY_REQUESTS
            return response_object, status

        return f(*args, **kwargs)

    return decorated


def method_path_combo_limiter(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        is_combo_allowed = RateLimit.is_combo_allowed(request.path, request.method)

        if not is_combo_allowed:
            response_object = {"status": "error", "message": "Too many requests"}
            status = HTTPStatus.TOO_MANY_REQUESTS
            return response_object, status

        return f(*args, **kwargs)

    return decorated


def token_required(f) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get("data")

        if not token:
            return data, status

        return f(*args, **kwargs)

    return decorated


def delivery_man_token_required(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = Auth.get_logged_in_user(request)

        token = data.get("data")

        if not token:
            return data, status

        admin = True if token.get("rol") >= 0 else False
        if not admin:
            response_object = {"status": "fail", "message": "admin token required"}
            return response_object, 401

        return f(*args, **kwargs)

    return decorated


def admin_token_required(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = Auth.get_logged_in_user(request)

        token = data.get("data")

        if not token:
            return data, status

        admin = True if token.get("rol") >= 2 else False
        if not admin:
            response_object = {"status": "fail", "message": "admin token required"}
            return response_object, 401

        return f(*args, **kwargs)

    return decorated
