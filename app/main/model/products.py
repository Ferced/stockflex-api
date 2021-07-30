
from .. import db, flask_bcrypt
from ..config import key
from typing import Union


class Products(db.Model):
    """ Products Model for storing products"""
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    path = db.Column(db.String(1000), nullable=False)
    ip = db.Column(db.String(50), nullable= False)
    time_started = db.Column(db.DateTime, nullable=False)
    time_finished = db.Column(db.DateTime, nullable=False)
    request = db.Column(db.String(5000), nullable=True)
    response = db.Column(db.String(5000), nullable=False)
    response_status = db.Column(db.Integer, nullable=False)