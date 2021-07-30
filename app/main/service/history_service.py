import uuid
import datetime
import requests
from app.main import db
from app.main.model.products import Products
from typing import Dict, Tuple

def get_all_history():
    return Products.query.all()

def get_history_by_id(id):
    return Products.query.filter_by(id=id).first()

