from flask_restx import Namespace, fields

class HistoryDto:
    api = Namespace('/history', description='product related operations')
    
class ProductsDto:
    api = Namespace('/', description='product related operations')
    products = api.model('auth_details', {
        'id': fields.Integer(required=True, description='id primarykey'),
        'path': fields.String(required=True, description='path provided by the user'),
        'ip': fields.String(required=True, description='ip from the user'),
        'time_started': fields.DateTime(required=True, description='Time requested by proxy'),
        'time_finished': fields.DateTime(required=True, description='Time response by meli'),
        'request': fields.String(required=True, description='request by the user'),
        'response': fields.String(required=True, description='response by meli api'),
        'response_status': fields.String(required=True, description='response status by meli api'),
        'method': fields.String(required=True, description='request method'),
    })