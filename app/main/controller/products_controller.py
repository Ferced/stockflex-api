from flask import request
from flask_restx import Resource

from app.main.util.decorator import ip_limiter,path_limiter
from ..util.dto import ProductsDto
from ..service.products_service import get_new_product
from typing import Dict, Tuple

api = ProductsDto.api

@api.route('/', defaults={'path': ''})
@api.route('/<path:path>')

class Product(Resource):
    @api.doc('get mercado libre api')
    @ip_limiter
    @path_limiter
    def get(self,path):
        data = request.json
        ip=request.remote_addr
        method=request.method
        response = get_new_product(data,path,ip,method)
        return response