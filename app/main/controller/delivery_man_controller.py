from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import DeliveryManDto
from ..service.delivery_man_service import (
    delete_delivery_man,
    save_new_delivery_man,
    get_all_delivery_men,
    update_delivery_man,
    delete_delivery_man,
)
from typing import Dict, Tuple

api = DeliveryManDto.api
_delivery_man = DeliveryManDto.delivery_man
_delivery_men = DeliveryManDto.delivery_men
# _update_delivery_man = DeliveryManDto.update_delivery_man


@api.route("/")
class DeliveryMan(Resource):
    @api.doc("list registered delivery_men")
    @admin_token_required
    @api.marshal_list_with(_delivery_men, envelope="data")
    def get(self):
        """List all registered delivery_men"""
        return get_all_delivery_men(request)

    @api.expect(_delivery_man, validate=True)
    @api.response(201, "DeliveryMan successfully created.")
    @admin_token_required
    @api.doc("create a new delivery_man")
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new DeliveryMan"""
        data = request.json
        return save_new_delivery_man(data=data)

    # @api.expect(_update_delivery_man, validate=True)
    @api.doc("update delivery_man")
    @admin_token_required
    def put(self):
        """Update delivery_men"""
        data = request.json
        return update_delivery_man(data)

    # @api.expect(_update_delivery_man, validate=True)
    @api.doc("delete delivery_man")
    @admin_token_required
    def delete(self):
        """delete delivery_men"""
        return delete_delivery_man(request)
