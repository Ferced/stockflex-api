from flask import request
from flask_restx import Resource

from ..util.dto import LogsDto, AccessLogsDto
from ..service.access_logs_service import AccessLogsService
from typing import Dict, Tuple

api = LogsDto.api
_access_log = AccessLogsDto.access_log


@api.route("/access_logs/")
class AccessLogList(Resource):
    @api.doc("list of logs")
    @api.marshal_list_with(_access_log, envelope="data")
    def get(self):
        """List all logs"""
        access_logs=AccessLogsService.get_all_logs(request)
        return access_logs

@api.route("/access_logs/all_errors")
class AccessLogList(Resource):
    @api.doc("list of logs errors")
    @api.marshal_list_with(_access_log, envelope="data")
    def get(self):
        """List all logs"""
        return AccessLogsService.get_all_logs_errors()


@api.route("/access_logs/count/<column>")
@api.param("column", "The AccessLog column")
@api.response(404, "AccessLog not found.")
class AccessLogCount(Resource):
    @api.doc("get a access_log count")
    def get(self,column):
        """get a access_log count"""
        path_count = AccessLogsService.get_logs_count(column)
        path_count = dict(path_count)
        if not path_count:
            api.abort(404)
        else:
            return path_count

@api.route("/access_logs/after_date_all/<date>")
@api.param("date", "The AccessLog date")
@api.response(404, "AccessLog not found.")
class AccessLogCount(Resource):
    @api.doc("get a access_log after the date")
    @api.marshal_with(_access_log)
    def get(self, date):
        """get a access_log given its method"""
        access_log = AccessLogsService.get_logs_after_date_all(date)
        if not access_log:
            api.abort(404)
        else:
            return access_log
