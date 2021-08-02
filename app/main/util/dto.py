from flask_restx import Namespace, fields

class LogsDto:
    api = Namespace('/access_logs', description='Logs related operations')
    
class AccessLogsDto:
    api = Namespace('/', description='AccessLog related operations')
    access_log = api.model('access_log_details', {
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