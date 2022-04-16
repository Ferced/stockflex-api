from logging import exception
import uuid
import datetime
from app.main.model.product_model import Product
from app.main.helpers.auth_helper import Auth
import ast

# from typing import Dict, Tuple


def save_new_product(request):
    data = request.json
    product = Product.objects(name=data["name"]).first()
    user = Auth.get_username_by_token(request.headers["Authorization"])
    if not product:
        new_product = Product(
            name=data["name"],
            min_price=data["min_price"],
            max_price=data["max_price"],
            unit_type=data["unit_type"],
            public_id=int(uuid.uuid4().int >> 100),
            registered_by=user["username"],
            registered_on=datetime.datetime.utcnow(),
        )
        new_product.save()
        response_object = {"status": "success", "message": "Successfully saved."}
        return response_object, 200
    else:
        response_object = {
            "status": "fail",
            "message": "Product already exists.",
        }
        return response_object, 409


def get_all_products(request):
    try:
        data = request.args.to_dict()
        data = ast.literal_eval(str(data).replace("[", "__").replace("]", ""))
        all_products = [product.to_json() for product in Product.objects.filter(**data)]
        return all_products
    except Exception as e:
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
            "description": str(e),
        }
        return response_object, 500


def update_product(data):
    try:
        product_to_update = Product.objects(name=data["name"]).first()
        product_to_update.update(**data)
        product_to_update.save()
        response_object = {"status": "success", "message": "Successfully updated."}
        return response_object, 200
    except Exception as e:
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
            "description": str(e),
        }
        return response_object, 500


def delete_product(request):
    try:
        product_to_delete = Product.objects(**request.args)
        product_to_delete.delete()
        response_object = {"status": "success", "message": "Successfully deleted."}
        return response_object, 200
    except Exception as e:
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
            "description": str(e),
        }
        return response_object, 500
