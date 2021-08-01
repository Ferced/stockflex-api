from flask import request
from flask_restx import Resource

from app.main.util.decorator import ip_limiter,path_limiter
from ..util.dto import AccessLogDto
from ..service.access_service import get_new_access
from typing import Dict, Tuple

api = AccessLogDto.api

@api.route('/', defaults={'path': ''})
@api.route('/<path:path>')
class Access(Resource):
    @api.doc('get mercado libre api')
    @ip_limiter
    @path_limiter
    def get(self,path):
        data = request.json
        ip=request.remote_addr
        method=request.method
        response = get_new_access(data,path,ip,method)
        return response

    @api.doc('get mercado libre api')
    @ip_limiter
    @path_limiter
    def post(self,path):
        data = request.json
        ip=request.remote_addr
        method=request.method
        response = get_new_access(data,path,ip,method)
        return response

    @api.doc('get mercado libre api')
    @ip_limiter
    @path_limiter
    def put(self,path):
        data = request.json
        ip=request.remote_addr
        method=request.method
        response = get_new_access(data,path,ip,method)
        return response
    
    @api.doc('get mercado libre api')
    @ip_limiter
    @path_limiter
    def delete(self,path):
        data = request.json
        ip=request.remote_addr
        method=request.method
        response = get_new_access(data,path,ip,method)
        return response