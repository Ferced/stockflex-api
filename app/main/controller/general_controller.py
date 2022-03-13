from flask import request
from flask_restx import Resource

from ..util.dto import PingDto

api = PingDto.api


@api.route("/")
class Ping(Resource):
    @api.doc("list registered clients")
    def get(self):
        """List all registered clients"""
        return "pong", 200
