from flask_restx import Namespace, fields


class ProductsDto:
    api = Namespace('/', description='product related operations')
    url_fields = {"url": fields.String}
