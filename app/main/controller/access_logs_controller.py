from flask import request
from flask_restx import Resource

from ..util.dto import LogsDto, AccessLogsDto
from ..service.access_logs_service import LogsService
from typing import Dict, Tuple

api = LogsDto.api
_access_log = AccessLogsDto.access_log


@api.route("/access_logs/")
class AccessLogsList(Resource):
    @api.doc("list of logs")
    @api.marshal_list_with(_access_log, envelope="data")
    def get(self):
        """List all logs"""
        return LogsService.get_all_logs()


@api.route("/access_logs/all_errors")
class AccessLogsList(Resource):
    @api.doc("list of logs errors")
    @api.marshal_list_with(_access_log, envelope="data")
    def get(self):
        """List all logs"""
        return LogsService.get_all_logs_errors()


@api.route("/access_logs/ip_count/")
@api.response(404, "AccessLog not found.")
class AccessLogsList(Resource):
    @api.doc("get a access_log count by ip")
    def get(self):
        """get a access_log count given its ip"""
        ip_count = LogsService.get_logs_ip_count()
        ip_count = dict(ip_count)
        if not ip_count:
            api.abort(404)
        else:
            return ip_count


@api.route("/access_logs/path_count/")
@api.response(404, "AccessLog not found.")
class AccessLogCount(Resource):
    @api.doc("get a access_log count by path")
    def get(self):
        """get a access_log count given its path"""
        path_count = LogsService.get_logs_path_count()
        path_count = dict(path_count)
        if not path_count:
            api.abort(404)
        else:
            return path_count


@api.route("/access_logs/method_count/")
@api.response(404, "AccessLog not found.")
class AccessLogCount(Resource):
    @api.doc("get a access_log count by method")
    def get(self):
        """get a access_log count given its method"""
        method_count = LogsService.get_logs_method_count()
        method_count = dict(method_count)
        if not method_count:
            api.abort(404)
        else:
            return method_count


@api.route("/access_logs/date_all/<date>")
@api.param("date", "The AccessLog date")
@api.response(404, "AccessLog not found.")
class AccessLogCount(Resource):
    @api.doc("get a access_log after the date")
    @api.marshal_with(_access_log)
    def get(self, date):
        """get a access_log given its method"""
        access_log = LogsService.get_logs_date_all(date)
        if not access_log:
            api.abort(404)
        else:
            return access_log


@api.route("/access_logs/search_by_ip/<ip>")
@api.param("ip", "The AccessLog ip")
@api.response(404, "AccessLog not found.")
class AccessLogCount(Resource):
    @api.doc("get a access_log by ip")
    @api.marshal_with(_access_log)
    def get(self, ip):
        """get a access_log given its ip"""
        access_log = LogsService.get_logs_by_ip(ip)
        if not access_log:
            api.abort(404)
        else:
            return access_log


@api.route("/access_logs/get_all_by_status/<status>")
@api.param("status", "The AccessLog status")
@api.response(404, "AccessLog not found.")
class AccessLogCount(Resource):
    @api.doc("get a access_log by status")
    @api.marshal_with(_access_log)
    def get(self, status):
        """get a access_log given its status"""
        access_log = LogsService.get_all_logs_by_status(status)
        if not access_log:
            api.abort(404)
        else:
            return access_log
