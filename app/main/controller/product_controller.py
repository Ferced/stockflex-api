from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required, delivery_man_token_required
from ..util.dto import ProductDto
from ..service.product_service import (
    delete_product,
    save_new_product,
    get_all_products,
    update_product,
    delete_product,
)
from typing import Dict, Tuple

api = ProductDto.api
_product = ProductDto.product


@api.route("/")
class Product(Resource):
    @api.doc("list registered products")
    @delivery_man_token_required
    @api.marshal_list_with(_product, envelope="data")
    def get(self):
        """List all registered products"""
        return get_all_products(request)

    @api.expect(_product, validate=True)
    @api.response(201, "Product successfully created.")
    @admin_token_required
    @api.doc("create a new product")
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Product"""
        return save_new_product(request)

    # @api.expect(_update_product, validate=True)
    @api.doc("update product")
    @admin_token_required
    def put(self):
        """Update products"""
        data = request.json
        return update_product(data)

    # @api.expect(_update_product, validate=True)
    @api.doc("delete product")
    @admin_token_required
    def delete(self):
        """delete products"""
        return delete_product(request)
