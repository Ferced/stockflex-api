from flask import request
from flask_restx import Resource

from app.main.util.decorator import ip_limiter, path_limiter
from ..util.dto import AccessLogsDto
from ..service.proxy_service import ProxyService

api = AccessLogsDto.api


@api.route("/", defaults={"path": ""})
@api.route("/<path:path>")
class ProxyController(Resource):
    @ip_limiter
    @path_limiter
    def get(self, path):
        data = request.json
        ip = request.remote_addr
        method = request.method
        response = ProxyService.handle_request(data, path, ip, method)
        return response

    @ip_limiter
    @path_limiter
    def post(self, path):
        data = request.json
        ip = request.remote_addr
        method = request.method
        response = ProxyService.handle_request(data, path, ip, method)
        return response

    @ip_limiter
    @path_limiter
    def put(self, path):
        data = request.json
        ip = request.remote_addr
        method = request.method
        response = ProxyService.handle_request(data, path, ip, method)
        return response

    @ip_limiter
    @path_limiter
    def delete(self, path):
        data = request.json
        ip = request.remote_addr
        method = request.method
        response = ProxyService.handle_request(data, path, ip, method)
        return response
