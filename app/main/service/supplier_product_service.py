from logging import exception
import uuid
import datetime
from app.main.model.supplier_product_model import SupplierProduct
from app.main.model.supplier_model import Supplier
from app.main.helpers.auth_helper import Auth
import ast


def save_new_product(request):
    data = request.json
    supplier = Supplier.objects(business_name=data["supplier_name"]).first()
    product = SupplierProduct.objects(
        name=data["name"], supplier_name=data["supplier_name"]
    ).first()
    user = Auth.get_username_by_token(request.headers["Authorization"])

    ## Validate if product already exists and the supplier exists
    if not product and supplier:
        new_product = SupplierProduct(
            name=data["name"],
            price=data["price"],
            supplier_name=data["supplier_name"],
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
            "message": "Validation error.",
            "description": "Product already exist"
            if product
            else "Supplier does not exist.",
        }
        return response_object, 409


def get_all_products(request):
    try:
        data = request.args.to_dict()
        data = ast.literal_eval(str(data).replace("[", "__").replace("]", ""))
        all_products = [
            product.to_json() for product in SupplierProduct.objects.filter(**data)
        ]
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
        product_to_update = SupplierProduct.objects(public_id=data["public_id"]).first()
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
        product_to_delete = SupplierProduct.objects(**request.args)
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


def validations():
    pass
