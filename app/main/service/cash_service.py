import ast
import uuid
from datetime import datetime, timedelta
from app.main.helpers.auth_helper import Auth
from app.main.model.cash_model import Cash


def save_new_record(request):
    try:
        # print(request.headers["Authorization"])
        data = request.json
        user = Auth.get_username_by_token(request.headers["Authorization"])

        new_record = Cash(
            payment=data["payment"],
            origin=data["origin"],
            destiny=data["destiny"],
            reason=data["reason"],
            entry_type=data["entry_type"],
            public_id=int(uuid.uuid4().int >> 100),
            registered_by=user["username"],
            registered_on=datetime.utcnow(),
        )
        new_record.save()
        response_object = {"status": "success", "message": "Successfully saved."}
        return response_object, 200
    except Exception as e:
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
            "description": str(e),
        }
        return response_object, 500


def get_all_records(request):
    data = request.args.to_dict()
    if "registered_on" in data:
        date_from = datetime.strptime(data["registered_on"], "%d/%m/%Y")
        date_to = datetime.strptime(data["registered_on"], "%d/%m/%Y") + timedelta(
            days=1
        )
        data["registered_on__gte"] = date_from.strftime("%Y-%-m-%-d %H:%M:%S")
        data["registered_on__lte"] = date_to.strftime("%Y-%-m-%-d %H:%M:%S")
        del data["registered_on"]

    data = ast.literal_eval(str(data).replace("[", "__").replace("]", ""))
    all_records = [record.to_json() for record in Cash.objects(**data)]
    return all_records


def update_record(data):
    try:
        record_to_update = Cash.objects(public_id=data["public_id"]).first()
        print("PRESAVE")
        record_to_update.update(**data)
        print("PRESAVE")
        record_to_update.save()
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
            "description": str(e),
        }
        return response_object, 500
