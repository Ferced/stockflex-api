from flask import request
from flask_restx import Resource

from ..util.dto import ProductsDto
from ..service.products_service import get_new_product
from typing import Dict, Tuple

api = ProductsDto.api

@api.route('/', defaults={'path': ''})
@api.route('/<path:path>')
class Product(Resource):
    @api.doc('get mercado libre api')
    def get(self,path):
        data = request.json
        ip=request.remote_addr
        response = get_new_product(data,path,ip)
        return response