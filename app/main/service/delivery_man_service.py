import uuid
import datetime
import json
from app.main import db
from app.main.model.delivery_man_model import DeliveryMan
from typing import Dict, Tuple


def save_new_delivery_man(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    delivery_man = DeliveryMan.objects(short_name=data["short_name"]).first()

    if not delivery_man:
        new_delivery_man = DeliveryMan(
            full_name=data["full_name"],
            short_name=data["short_name"],
            email=data["email"],
            phone_number=data["phone_number"],
            public_id=int(uuid.uuid4().int >> 100),
            registered_on=datetime.datetime.utcnow(),
        )
        new_delivery_man.save()
        response_object = {"status": "success", "message": "Successfully saved."}
        return response_object, 200
    else:
        response_object = {
            "status": "fail",
            "message": "DeliveryMan already exists.",
        }
        return response_object, 409


def get_all_delivery_men(request):
    all_delivery_men = [
        delivery_man.to_json() for delivery_man in DeliveryMan.objects(**request.args)
    ]
    return all_delivery_men


def update_delivery_man(data):
    try:
        delivery_man_to_update = DeliveryMan.objects(
            public_id=data["public_id"]
        ).first()
        try:
            del data["public_id"]
            del data["registered_on"]
        except:
            pass
        delivery_man_to_update.update(**data)
        delivery_man_to_update.save()
        response_object = {"status": "success", "message": "Successfully updated."}
        return response_object, 200
    except Exception as e:
        print(e)
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
        }
        return response_object, 500


def delete_delivery_man(request):
    try:
        deliveryMan_to_delete = DeliveryMan.objects(**request.args)
        deliveryMan_to_delete.delete()
        response_object = {"status": "success", "message": "Successfully deleted."}
        return response_object, 200
    except Exception as e:
        print(e)
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
        }
        return response_object, 500
