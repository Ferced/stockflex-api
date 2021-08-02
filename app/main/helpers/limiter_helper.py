from datetime import datetime, timedelta

from app.main.model.access_logs import AccessLogs
from app.main.helpers.constants.constants_general import ConstantsLimiter
from typing import Dict, Tuple


class Limiter:
    @staticmethod
    def ip_limiter(request):
        try:
            # fetch the access log data
            access_log = AccessLogs.query.filter(
                AccessLogs.ip == request.remote_addr,
                AccessLogs.time_finished >= datetime.now() - timedelta(hours=1),
            ).all()
            if len(access_log) > ConstantsLimiter.ip_limit_per_hour:
                response_object = {"status": "fail", "message": "Too many re quests"}
                return response_object, 429
            else:
                response_object = {"status": "success", "message": "success"}
                return response_object, 200
        except Exception as e:
            print(e)
            response_object = {"status": "fail", "message": "Internal proxy error"}
            return response_object, 500

    @staticmethod
    def path_limiter(request):
        try:
            # fetch the access_log data
            access_log = AccessLogs.query.filter_by(path=request.path[1:]).all()
            if len(access_log) > ConstantsLimiter.path_limit_per_hour:
                response_object = {"status": "fail", "message": "Too many requests"}
                return response_object, 429
            else:
                response_object = {"status": "success", "message": "success"}
                return response_object, 200
        except Exception as e:
            print(e)
            response_object = {"status": "fail", "message": "Internal proxy error"}
            return response_object, 500
