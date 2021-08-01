from flask import request
from flask_restx import Resource

from ..util.dto import HistoryDto,AccessLogDto
from ..service.access_logs_service import get_all_logs, get_logs_by_id, get_logs_by_ip,get_logs_ip_count,get_logs_path_count,get_logs_method_count,get_logs_date_count
from typing import Dict, Tuple

api = HistoryDto.api
_access_log = AccessLogDto.access_log

@api.route('/access_logs/')
class AccessLogsList(Resource):
    @api.doc('list of logs')
    #@admin_token_required
    @api.marshal_list_with(_access_log, envelope='data')
    def get(self):
        """List all logs"""
        return get_all_logs()

@api.route('/access_logs/ip_count/')
@api.response(404, 'AccessLog not found.')
class AccessLogsList(Resource):
    @api.doc('get a access_log count by ip')
    def get(self):
        """get a access_log count given its ip"""
        ip_count = get_logs_ip_count()
        ip_count = dict(ip_count)
        if not ip_count:
            api.abort(404)
        else:
            return ip_count

@api.route('/access_logs/path_count/')
@api.response(404, 'AccessLog not found.')
class AccessLogCount(Resource):
    @api.doc('get a access_log count by path')
    def get(self):
        """get a access_log count given its path"""
        path_count = get_logs_path_count()
        path_count = dict(path_count)
        if not path_count:
            api.abort(404)
        else:
            return path_count

@api.route('/access_logs/method_count/')
@api.response(404, 'AccessLog not found.')
class AccessLogCount(Resource):
    @api.doc('get a access_log count by method')
    def get(self):
        """get a access_log count given its method"""
        method_count = get_logs_method_count()
        method_count = dict(method_count)
        if not method_count:
            api.abort(404)
        else:
            return method_count

@api.route('/access_logs/date_count/')
@api.response(404, 'AccessLog not found.')
class AccessLogCount(Resource):
    @api.doc('get a access_log count by date')
    def get(self):
        """get a access_log given its method"""
        date_count = get_logs_date_count()
        date_count = dict(date_count)
        if not date_count:
            api.abort(404)
        else:
            return date_count

@api.route('/access_logs/search_by_ip/<ip>')
@api.param('ip', 'The AccessLog ip')
@api.response(404, 'AccessLog not found.')
class AccessLogCount(Resource):
    @api.doc('get a access_log by ip')
    @api.marshal_with(_access_log)
    def get(self,ip):
        """get a access_log given its ip"""
        access_log = get_logs_by_ip(ip)
        if not access_log:
            api.abort(404)
        else:
            return access_log

