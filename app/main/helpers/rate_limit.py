from datetime import datetime, timedelta
from http import HTTPStatus

from mongoengine.queryset.visitor import Q
from app.main.model.access_logs_model import AccessLog
from app.main.helpers.constants.constants_general import LimiterConstants
from typing import Dict, Tuple

# TODO: No filtra por la ultima hora.
class RateLimit:
    @staticmethod
    def is_ip_allowed(request):
        date = datetime.now() - timedelta(hours=1)
        all_access_logs = [
            access_log.to_json()
            for access_log in AccessLog.objects(
                Q(ip__exact=request.remote_addr) and Q(request_start_time__gte=date)
            )
        ]
        if len(all_access_logs) > LimiterConstants.ip_limit_per_hour:
            return False
        return True

    @staticmethod
    def is_path_allowed(request):
        date = datetime.now() - timedelta(hours=1)
        all_access_logs = [
            access_log.to_json()
            for access_log in AccessLog.objects(
                Q(path__exact=request.path[1:]) and Q(request_start_time__gte=date)
            )
        ]
        if len(all_access_logs) > LimiterConstants.path_limit_per_hour:
            return False
        return True

    @staticmethod
    def is_combo_allowed(request):
        date = datetime.now() - timedelta(hours=1)
        all_access_logs = [
            access_log.to_json()
            for access_log in AccessLog.objects(
                Q(path__exact=request.path[1:])
                and Q(ip__exact=request.remote_addr)
                and Q(request_start_time__gte=date)
            )
        ]
        if len(all_access_logs) > LimiterConstants.path_limit_per_hour:
            return False
        return True
