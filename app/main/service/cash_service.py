import uuid
import datetime
import json
from app.main import db
from app.main.helpers.auth_helper import Auth
from app.main.model.cash_model import Cash
from typing import Dict, Tuple


def save_new_record(request):
    # print(request.headers["Authorization"])
    data = request.json
    user = Auth.get_username_by_token(request.headers["Authorization"])

    new_record = Cash(
        payment=data["payment"],
        origin=data["origin"],
        destiny=data["destiny"],
        reason=data["reason"],
        type=data["type"],
        public_id=int(uuid.uuid4().int >> 100),
        registered_by=user["username"],
        registered_on=datetime.datetime.utcnow(),
    )
    new_record.save()
    response_object = {"status": "success", "message": "Successfully saved."}
    return response_object, 200


def get_all_records(request):
    all_records = [record.to_json() for record in Cash.objects(**request.args)]
    return all_records


def update_record(data):
    try:
        record_to_update = Cash.objects(public_id=data["public_id"]).first()
        record_to_update.update(**data)
        record_to_update.save()
        response_object = {"status": "success", "message": "Successfully updated."}
        return response_object, 200
    except Exception as e:
        print(e)
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
        }
        return response_object, 500


def delete_record(request):

    try:
        record_to_delete = Cash.objects(**request.args)
        record_to_delete.delete()
        response_object = {"status": "success", "message": "Successfully deleted."}
        return response_object, 200
    except Exception as e:
        print(e)
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
        }
        return response_object, 500
