import uuid
import datetime

from app.main import db
from app.main.model.user_model import User
from typing import Dict, Tuple


def save_new_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    user = User.objects(username=data["username"])
    if not user:
        new_user = User(
            email=data["email"],
            rol=data["rol"],
            username=data["username"],
            password=data["password"],
            public_id=int(uuid.uuid4().int >> 100),
            registered_on=datetime.datetime.utcnow(),
        )
        new_user.save()
        return generate_token(new_user)
    else:
        response_object = {
            "status": "fail",
            "message": "User already exists. Please Log in.",
        }
        return response_object, 409


def get_all_users(request):
    all_users = [user.to_json() for user in User.objects(**request.args)]
    return all_users


def update_user(data):
    try:
        user_to_update = User.objects(username=data["username"]).first()
        user_to_update.email = data["email"]
        user_to_update.rol = data["rol"]
        try:
            user_to_update.password = data["password"]
        except Exception as e:
            pass
        user_to_update.save()
        response_object = {"status": "success", "message": "Successfully updated."}
        return response_object, 200
    except Exception as e:
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
        }
        return response_object, 500


def delete_user(request):

    try:
        user_to_delete = User.objects(**request.args)
        user_to_delete.delete()
        response_object = {"status": "success", "message": "Successfully deleted."}
        return response_object, 200
    except Exception as e:
        print(e)
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
        }
        return response_object, 500


def generate_token(user: User) -> Tuple[Dict[str, str], int]:
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(user.public_id)
        response_object = {
            "status": "success",
            "message": "Successfully registered.",
            "Authorization": auth_token.decode(),
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
        }
        return response_object, 500
