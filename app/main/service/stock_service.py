from logging import exception
import uuid
import datetime
import json
from app.main import db
from app.main.model.stock_model import Stock
from app.main.model.supplier_model import Supplier
from app.main.model.client_model import Client
from app.main.helpers.auth_helper import Auth

# from typing import Dict, Tuple


def save_new_stock(request):
    # print(request.headers["Authorization"])
    data = request.json
    user = Auth.get_username_by_token(request.headers["Authorization"])

    try:
        if data["entry_type"]:
            business = Supplier.objects(business_name=data["business_name"]).first()
        else:
            business = Client.objects(business_name=data["business_name"]).first()
        if business:
            new_stock = Stock(
                product_name=data["product_name"],
                amount=data["amount"],
                amount_type=data["amount_type"],
                payment=data["payment"],
                business_name=data["business_name"],
                entry_type=data["entry_type"],
                public_id=int(uuid.uuid4().int >> 100),
                registered_by=user["username"],
                registered_on=datetime.datetime.utcnow(),
            )
            new_stock.save()
            response_object = {
                "status": "success",
                "message": "Successfully saved.",
            }
            return response_object, 200
        else:
            response_object = {
                "status": "fail",
                "message": "Supplier not registered.",
            }
            return response_object, 409
    except Exception as e:
        print(e)
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
        }
        return response_object, 500


def get_all_stocks(request):
    all_stocks = [stock.to_json() for stock in Stock.objects(**request.args)]
    return all_stocks


def update_stock(data):
    del data["registered_on"]
    del data["registered_by"]
    try:
        stock_to_update = Stock.objects(public_id=data["public_id"]).first()
        del data["public_id"]
        stock_to_update.update(**data)
        stock_to_update.save()
        response_object = {"status": "success", "message": "Successfully updated."}
        return response_object, 200
    except Exception as e:
        print(e)
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
        }
        return response_object, 500


def delete_stock(request):
    try:
        stock_to_delete = Stock.objects(**request.args).first()
        stock_to_delete.delete()
        response_object = {"status": "success", "message": "Successfully deleted."}
        return response_object, 200

    except Exception as e:
        print(e)
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
        }
        return response_object, 500
