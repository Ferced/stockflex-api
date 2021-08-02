import uuid
import datetime
import requests
from sqlalchemy import func
from app.main import db
from app.main.model.access_logs import AccessLogs
from typing import Dict, Tuple


class LogsService:
    @staticmethod
    def get_all_logs():
        return AccessLogs.query.all()

    @staticmethod
    def get_all_logs_by_status(status):
        return AccessLogs.query.filter_by(response_status=status).all()

    @staticmethod
    def get_logs_date_all(date):
        return AccessLogs.query.filter(AccessLogs.time_started >= date).all()

    @staticmethod
    def get_all_logs_errors():
        return AccessLogs.query.filter(AccessLogs.response_status != 200).all()

    @staticmethod
    def get_logs_by_id(id):
        return AccessLogs.query.filter_by(id=id).first()

    @staticmethod
    def get_logs_by_ip(ip):
        return AccessLogs.query.filter_by(ip=ip).all()

    @staticmethod
    def get_logs_ip_count():
        return (
            AccessLogs.query.with_entities(AccessLogs.ip, func.count(AccessLogs.ip))
            .group_by(AccessLogs.ip)
            .all()
        )

    @staticmethod
    def get_logs_path_count():
        return (
            AccessLogs.query.with_entities(AccessLogs.path, func.count(AccessLogs.path))
            .group_by(AccessLogs.path)
            .all()
        )

    @staticmethod
    def get_logs_method_count():
        return (
            AccessLogs.query.with_entities(
                AccessLogs.method, func.count(AccessLogs.method)
            )
            .group_by(AccessLogs.method)
            .all()
        )
