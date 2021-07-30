import uuid
import datetime
import requests
from app.main import db
from app.main.model.products import Products
from typing import Dict, Tuple

#TRANSFORMAR EN CLASS
def get_new_product(data,path,ip,method):
    try:
        time_request_start = datetime.datetime.utcnow()
        response_object =  get_meli_api(path,data)
        response_status = response_object['status']

        new_product = Products(
            path = path,
            ip = ip,
            time_started = time_request_start,
            time_finished = datetime.datetime.utcnow(),
            request = str(data),
            response = str(response_object),
            response_status = response_status,
            method=method,
        )

        save_changes(new_product)

        
        return response_object,response_status

    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'internal proxy error.',
            'error_message':e
        }
        return response_object, 500
def get_meli_api(path,data):
    url = "https://api.mercadolibre.com/"+path
    params = data
    resp = requests.get(url=url, params=params)
    response_object = resp.json()
    return response_object
    

# def get_all_products():
#     return Products.query.all()


# def get_a_product(product_id):
#     return Products.query.filter_by(product_id=product_id).first()


# #borrar
# def get_a_product_by_id(id):
#     return Products.query.filter_by(id=id).first()


def save_changes(data: Products) -> None:
    db.session.add(data)
    db.session.commit()

