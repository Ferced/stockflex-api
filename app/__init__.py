from flask_restx import Api
from flask import Blueprint

# from .main.controller.proxy_controller import api as proxy_ns
# from .main.controller.access_logs_controller import api as access_logs_ns
from .main.controller.user_controller import api as user_ns
from .main.controller.client_controller import api as client_ns
from .main.controller.supplier_controller import api as supplier_ns
from .main.controller.stock_controller import api as stock_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.delivery_man_controller import api as delivery_man_ns
from .main.controller.cash_controller import api as cash_ns

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="conrnalito-api",
    version="1.0",
    description="reverse proxy para la api de mercado libre",
)

# api.add_namespace(access_logs_ns, path="/proxy")
api.add_namespace(user_ns, path="/user")
api.add_namespace(client_ns, path="/client")
api.add_namespace(supplier_ns, path="/supplier")
api.add_namespace(stock_ns, path="/stock")
api.add_namespace(delivery_man_ns, path="/delivery-man")
api.add_namespace(cash_ns, path="/cash")
api.add_namespace(auth_ns)
