from .. import db, flask_bcrypt
from ..config import key


class AccessLog(db.Model):
    """Products Model for storing access_logs"""

    __tablename__ = "access_logs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    path = db.Column(db.String(1000), nullable=False)
    ip = db.Column(db.String(50), nullable=False)
    request_start_time = db.Column(db.DateTime, nullable=False)
    request_end_time = db.Column(db.DateTime, nullable=False)
    request = db.Column(db.String(5000), nullable=True)
    response = db.Column(db.String(5000), nullable=False)
    response_status = db.Column(db.Integer, nullable=False)
    method = db.Column(db.String(50), nullable=False)

    def __getitem__(self, key):
        return self.__dict__[key]
