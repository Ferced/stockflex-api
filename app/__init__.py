from flask_restx import Api
from flask import Blueprint

from .main.controller.products_controller import api as products_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='reverse-proxy-meli',
          version='1.0',
          description='reverse proxy para la api de mercado libre'
          )

api.add_namespace(products_ns,path=None)
