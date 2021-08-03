from datetime import datetime, timedelta
from http import HTTPStatus
from app.main.model.access_logs import AccessLog
from app.main.helpers.constants.constants_general import LimiterConstants
from typing import Dict, Tuple


class RateLimit:
    @staticmethod
    def is_ip_allowed(request):

        # fetch the access log data
        access_log = AccessLog.query.filter(
            AccessLog.request_end_time >= datetime.now() - timedelta(hours=1),
        ).all()
        # dict {"ip":22,"path":30,"combo":12}
        if len(access_log) > LimiterConstants.ip_limit_per_hour:
            return False
        return True

    @staticmethod
    def is_ip_allowed(request):

        # fetch the access log data
        access_log = AccessLog.query.filter(
            AccessLog.ip == request.remote_addr,
            AccessLog.request_end_time >= datetime.now() - timedelta(hours=1),
        ).all()
        if len(access_log) > LimiterConstants.ip_limit_per_hour:
            return False
        return True

    @staticmethod
    def is_path_allowed(request):

        # fetch the access_log data
        access_log = AccessLog.query.filter(
            AccessLog.path == request.path[1:],
            AccessLog.request_end_time >= datetime.now() - timedelta(hours=1),
        ).all()
        if len(access_log) > LimiterConstants.path_limit_per_hour:
            return False
        return True

    @staticmethod
    def is_combo_allowed(request):
        # fetch the access_log data
        access_log = AccessLog.query.filter(
            AccessLog.ip == request.remote_addr,
            AccessLog.path == request.path[1:],
            AccessLog.request_end_time >= datetime.now() - timedelta(hours=1),
        ).all()
        if len(access_log) > LimiterConstants.combo_limit_per_hour:
            return False
        return True
