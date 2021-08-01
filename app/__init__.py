from flask_restx import Api
from flask import Blueprint

from .main.controller.access_controller import api as access_ns
from .main.controller.access_logs_controller import api as access_logs_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='reverse-proxy-meli',
          version='1.0',
          description='reverse proxy para la api de mercado libre'
          )

api.add_namespace(access_logs_ns,path='/proxy')
api.add_namespace(access_ns,path=None)


