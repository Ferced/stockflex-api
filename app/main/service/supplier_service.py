import ast
import uuid
import datetime
import json
from app.main import db
from querystring_parser import parser
from app.main.model.supplier_model import Supplier
from typing import Dict, Tuple


def save_new_supplier(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    supplier = Supplier.objects(business_name=data["business_name"]).first()

    if not supplier:
        new_supplier = Supplier(
            referrer=data["referrer"],
            business_name=data["business_name"],
            address=data["address"],
            delivery_man=data["delivery_man"],
            registered_on=datetime.datetime.utcnow(),
        )
        new_supplier.save()
        response_object = {"status": "success", "message": "Successfully saved."}
        return response_object, 200
    else:
        response_object = {
            "status": "fail",
            "message": "Supplier already exists.",
        }
        return response_object, 409


def get_all_suppliers(request):
    data = request.args.to_dict()
    data = ast.literal_eval(str(data).replace("[", "__").replace("]", ""))
    all_suppliers = [supplier.to_json() for supplier in Supplier.objects(**data)]
    return all_suppliers


def update_supplier(data):
    try:
        supplier_to_update = Supplier.objects(
            business_name=data["business_name"]
        ).first()
        supplier_to_update.update(**data)
        supplier_to_update.save()
        response_object = {"status": "success", "message": "Successfully updated."}
        return response_object, 200
    except Exception as e:
        print(e)
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
            "description": str(e),
        }
        return response_object, 500


def delete_supplier(request):

    try:
        supplier_to_delete = Supplier.objects(**request.args)
        supplier_to_delete.delete()
        response_object = {"status": "success", "message": "Successfully deleted."}
        return response_object, 200
    except Exception as e:
        print(e)
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
            "description": str(e),
        }
        return response_object, 500
