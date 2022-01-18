from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import StockDto
from ..service.stock_service import (
    delete_stock,
    save_new_stock,
    get_all_stocks,
    update_stock,
    delete_stock,
)
from typing import Dict, Tuple

api = StockDto.api
_stock = StockDto.stock
_update_stock = StockDto.update_stock


@api.route("/")
class Stock(Resource):
    @api.doc("list registered stocks")
    @admin_token_required
    @api.marshal_list_with(_stock, envelope="data")
    def get(self):
        """List all registered stocks"""
        return get_all_stocks(request)

    @api.expect(_stock, validate=True)
    @api.response(201, "Stock successfully created.")
    @api.doc("create a new stock")
    @admin_token_required
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Stock"""
        return save_new_stock(request)

    @api.expect(_update_stock, validate=True)
    @api.doc("update stock")
    @admin_token_required
    def put(self):
        """Update stocks"""
        data = request.json
        return update_stock(data)

    # @api.expect(_update_stock, validate=True)
    @api.doc("delete stock")
    @admin_token_required
    def delete(self):
        """delete stocks"""
        return delete_stock(request)
