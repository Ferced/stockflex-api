import uuid
import datetime
import requests
from app.main import db
from app.main.model.products import Products
from app.main.helpers.constants.constants_general import ConstantsGeneral
from typing import Dict, Tuple

#TRANSFORMAR EN CLASS
def get_new_product(data,path,ip,method):
    try:
        time_request_start = datetime.datetime.now()
        response_object,response_status =  get_meli_api(path,data)

        new_product = Products(
            path = path,
            ip = ip,
            time_started = time_request_start,
            time_finished = datetime.datetime.now(),
            request = str(data),
            response = str(response_object),
            response_status = response_status,
            method=method
        )
        
        save_changes(new_product) 
        return response_object,response_status

    except Exception as e:
        response_status = 500
        response_object = {
            'message': 'internal proxy error',
            'error':e,
            'status': response_status,
        }
        return response_object, response_status

def get_meli_api(path,data):
    url = ConstantsGeneral.url_api_meli+path
    params = data
    resp = requests.get(url=url, params=params)
    response_object = resp.json()
    return response_object,resp.status_code
    
def save_changes(data: Products) -> None:
    db.session.add(data)
    db.session.commit()

