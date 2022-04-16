from app.main.model.user_model import User
from ..service.blacklist_service import save_token
from typing import Dict, Tuple


class Auth:
    @staticmethod
    def login_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            # fetch the user data
            try:
                user = User.objects(username=data["username"]).first()
            except Exception as e:
                return {"message": "Invalid credentials"}, 401
            if user and user.check_password(data["password"]):
                auth_token = User.encode_auth_token(user.public_id)
                if auth_token:
                    response_object = {
                        "data": user.to_json(),
                        "status": "success",
                        "message": "Successfully logged in.",
                        "Authorization": auth_token.decode(),
                    }
                    return response_object, 200
            else:
                response_object = {
                    "status": "fail",
                    "message": "email or password does not match.",
                }
                return response_object, 401

        except Exception as e:
            response_object = {"status": "fail", "message": "Try again"}
            return response_object, 500

    @staticmethod
    def logout_user(data: str) -> Tuple[Dict[str, str], int]:
        auth_token = data
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {"status": "fail", "message": resp}
                return response_object, 401
        else:
            response_object = {
                "status": "fail",
                "message": "Provide a valid auth token.",
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get("Authorization")

        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.objects(public_id=resp).first()
                response_object = {
                    "status": "success",
                    "data": {
                        "user_public_id": user.public_id,
                        "email": user.email,
                        "rol": user.rol,
                        "registered_on": str(user.registered_on),
                    },
                }
                return response_object, 200
            response_object = {"status": "fail", "message": resp}
            return response_object, 401
        else:
            response_object = {
                "status": "fail",
                "message": "Provide a valid auth token.",
            }
            return response_object, 401

    @staticmethod
    def get_username_by_token(token):
        resp = User.decode_auth_token(token)
        if not isinstance(resp, str):
            user = User.objects(public_id=resp).first()
            response = {
                "username": user.username,
                "public_id": user.public_id,
                "email": user.email,
                "rol": user.rol,
                "registered_on": str(user.registered_on),
            }
            return response
        return None
