from mongoengine.queryset.visitor import Q
from app.main.model.access_logs_model import AccessLog


class AccessLogsService:
    @staticmethod
    def get_all_logs(request):
        all_access_logs = [
            access_log.to_json() for access_log in AccessLog.objects(**request.args)
        ]
        return all_access_logs

    @staticmethod
    def get_logs_after_date(date):
        all_access_logs = [
            access_log.to_json()
            for access_log in AccessLog.objects((Q(request_start_time__gte=date)))
        ]
        return all_access_logs

    @staticmethod
    def get_all_logs_errors():
        all_access_logs = [
            access_log.to_json()
            for access_log in AccessLog.objects(response_status__ne=200)
        ]
        return all_access_logs

    @staticmethod
    def get_logs_count(column):
        return AccessLog.objects.item_frequencies(column)
