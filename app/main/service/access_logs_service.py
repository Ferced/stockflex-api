import uuid
import datetime
import requests
from sqlalchemy import func
from app.main import db
from app.main.model.access_logs import AccessLog
from typing import Dict, Tuple


class AccessLogsService:
    @staticmethod
    def get_all_logs(request):
        return AccessLog.query.filter_by(**request.args).all()

    @staticmethod
    def get_logs_after_date_all(date):
        return AccessLog.query.filter(AccessLog.time_started >= date).all()

    @staticmethod
    def get_logs_date_count(date):
        return AccessLog.query.filter(AccessLog.time_started >= date).all()

    @staticmethod
    def get_all_logs_errors():
        return AccessLog.query.filter(AccessLog.response_status != 200).all() #a chequear 

    @staticmethod
    def get_logs_count(column):
        return (
            AccessLog.query.with_entities(getattr(AccessLog,column), func.count(getattr(AccessLog,column))) #posible filtro count
            .group_by(getattr(AccessLog,column))
            .all()
        )