from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import ProductDto
from ..service.history_service import get_all_history, get_history_by_id
from typing import Dict, Tuple

api = ProductDto.api
_product = ProductDto.product



@api.route('/')
class HistoryList(Resource):
    @api.doc('list of history')
    #@admin_token_required
    @api.marshal_list_with(_product, envelope='data')
    def get(self):
        """List all history"""
        return get_all_history()

@api.route('/search')
@api.param('product_id', 'The Product identifier')
@api.response(404, 'Product not found.')
class Product(Resource):
    @api.doc('get a product')
    @api.marshal_with(_product)
    def get(self):
        """get a product given its identifier"""
        product_id = request.args.get('product_id')
        product = get_history_by_id(product_id)
        if not product:
            api.abort(404)
        else:
            return product
