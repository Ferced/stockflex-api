from .. import db, flask_bcrypt
from ..config import key


class AccessLog(db.Document):
    """AccessLog Model for storing access_logs"""

    path = db.StringField()
    ip = db.StringField()
    request_start_time = db.DateTimeField()
    request_end_time = db.DateTimeField()
    request = db.StringField()
    response = db.StringField()
    response_status = db.IntField()
    method = db.StringField()

    def to_json(self):
        return {
            "path": self.path,
            "ip": self.ip,
            "request_start_time": self.request_start_time,
            "request_end_time": self.request_end_time,
            "request": self.request,
            "response": self.response,
            "response_status": self.response_status,
            "method": self.method,
        }
