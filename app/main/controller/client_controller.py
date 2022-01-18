from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import ClientDto
from ..service.client_service import (
    delete_client,
    save_new_client,
    get_all_clients,
    update_client,
    delete_client,
)
from typing import Dict, Tuple

api = ClientDto.api
_client = ClientDto.client
_clients = ClientDto.clients
_update_client = ClientDto.update_client


@api.route("/")
class Client(Resource):
    @api.doc("list registered clients")
    @admin_token_required
    @api.marshal_list_with(_clients, envelope="data")
    def get(self):
        """List all registered clients"""
        return get_all_clients(request)

    @api.expect(_client, validate=True)
    @api.response(201, "Client successfully created.")
    @admin_token_required
    @api.doc("create a new client")
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Client"""
        data = request.json
        return save_new_client(data=data)

    # @api.expect(_update_client, validate=True)
    @api.doc("update client")
    @admin_token_required
    def put(self):
        """Update clients"""
        data = request.json
        return update_client(data)

    # @api.expect(_update_client, validate=True)
    @api.doc("delete client")
    @admin_token_required
    def delete(self):
        """delete clients"""
        return delete_client(request)
