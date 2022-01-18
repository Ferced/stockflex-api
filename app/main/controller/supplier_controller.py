from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import SupplierDto
from ..service.supplier_service import (
    delete_supplier,
    save_new_supplier,
    get_all_suppliers,
    update_supplier,
    delete_supplier,
)
from typing import Dict, Tuple

api = SupplierDto.api
_supplier = SupplierDto.supplier
_suppliers = SupplierDto.suppliers
_update_supplier = SupplierDto.update_supplier


@api.route("/")
class Supplier(Resource):
    @api.doc("list registered suppliers")
    @admin_token_required
    @api.marshal_list_with(_suppliers, envelope="data")
    def get(self):
        """List all registered suppliers"""
        return get_all_suppliers(request)

    @api.expect(_supplier, validate=True)
    @api.response(201, "Supplier successfully created.")
    @admin_token_required
    @api.doc("create a new supplier")
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Supplier"""
        data = request.json
        return save_new_supplier(data=data)

    # @api.expect(_update_supplier, validate=True)
    @api.doc("update supplier")
    @admin_token_required
    def put(self):
        """List all registered suppliers"""
        data = request.json
        return update_supplier(data)

    # @api.expect(_update_supplier, validate=True)
    @api.doc("delete supplier")
    @admin_token_required
    def delete(self):
        """delete suppliers"""
        return delete_supplier(request)
