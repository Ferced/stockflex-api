import uuid
import datetime
import json
from app.main import db
from app.main.model.client_model import Client
from typing import Dict, Tuple
import ast


def save_new_client(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    try:
        client = Client.objects(business_name=data["business_name"]).first()

        if not client:
            new_client = Client(
                referrer=data["referrer"],
                business_name=data["business_name"],
                address=data["address"],
                delivery_man=data["delivery_man"],
                debt_limit=data["debt_limit"],
                registered_on=datetime.datetime.utcnow(),
            )
            new_client.save()
            response_object = {"status": "success", "message": "Successfully saved."}
            return response_object, 200
        else:
            response_object = {
                "status": "fail",
                "message": "Client already exists.",
            }
            return response_object, 409
    except Exception as e:
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
            "description": str(e),
        }
        return response_object, 500


def get_all_clients(request):
    try:
        data = request.args.to_dict()
        data = ast.literal_eval(str(data).replace("[", "__").replace("]", ""))
        print(
            "data after replace: ",
            data,
        )
        all_clients = [client.to_json() for client in Client.objects.filter(**data)]
        return all_clients
    except Exception as e:
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
            "description": str(e),
        }
        return response_object, 500


def update_client(data):
    try:
        client_to_update = Client.objects(business_name=data["business_name"]).first()
        client_to_update.update(**data)
        client_to_update.save()
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


def delete_client(request):

    try:
        client_to_delete = Client.objects(**request.args)
        client_to_delete.delete()
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
