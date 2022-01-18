from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import UserDto
from ..service.user_service import (
    save_new_user,
    get_all_users,
    update_user,
    delete_user,
)
from typing import Dict, Tuple

api = UserDto.api
_user = UserDto.user
_users = UserDto.users
_update_user = UserDto.update_user


@api.route("/")
class User(Resource):
    @api.doc("list registered users")
    @admin_token_required
    @api.marshal_list_with(_users, envelope="data")
    def get(self):
        """List all registered users"""
        return get_all_users(request)

    @api.expect(_user, validate=True)
    @api.response(201, "User successfully created.")
    @api.doc("create a new user")
    @admin_token_required
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new User"""
        data = request.json
        return save_new_user(data=data)

    # @api.expect(_update_user, validate=True)
    @api.doc("update user")
    @admin_token_required
    def put(self):
        """update user"""
        data = request.json
        return update_user(data)

    # @api.expect(_update_user, validate=True)
    @api.doc("delete user")
    @admin_token_required
    def delete(self):
        """delete user"""
        return delete_user(request)
