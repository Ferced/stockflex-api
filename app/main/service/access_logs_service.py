import uuid
import datetime
import requests
from sqlalchemy import func
from app.main import db
from app.main.model.access_logs import AccessLogs
from typing import Dict, Tuple

def get_all_logs():
    return AccessLogs.query.all()

def get_logs_by_id(id):
    return AccessLogs.query.filter_by(id=id).first()

def get_logs_by_ip(ip):
    return AccessLogs.query.filter_by(ip=ip).all()

def get_logs_ip_count():
    return AccessLogs.query.with_entities(AccessLogs.ip, func.count(AccessLogs.ip)).group_by(AccessLogs.ip).all()

def get_logs_path_count():
    return AccessLogs.query.with_entities(AccessLogs.path, func.count(AccessLogs.path)).group_by(AccessLogs.path).all()

def get_logs_date_count():
    return AccessLogs.query.with_entities(AccessLogs.time_started, func.count(AccessLogs.time_started)).group_by(AccessLogs.time_started).all()

def get_logs_method_count():
    return AccessLogs.query.with_entities(AccessLogs.method, func.count(AccessLogs.method)).group_by(AccessLogs.method).all()
