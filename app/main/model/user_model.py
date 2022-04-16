from typing_extensions import Required
from .. import db, flask_bcrypt
import datetime
from ..config import key
from app.main.model.blacklist_model import BlacklistToken
import jwt
from typing import Union


class User(db.Document):
    email = db.EmailField(unique=True, required=True)
    username = db.StringField(max_length=30, unique=True, required=True)
    password = db.BinaryField(max_length=255, required=True)
    rol = db.IntField(required=True)
    public_id = db.IntField(required=True)
    registered_on = db.DateTimeField(required=True)

    def to_json(self):
        return {
            "email": self.email,
            "username": self.username,
            "rol": self.rol,
            "public_id": self.public_id,
        }

    def clean(self):
        if not self.hashed(self.password):
            self.password = flask_bcrypt.generate_password_hash(self.password)

    def hashed(self, password):
        return False  # boolean check of whether the password is already hashed

    def check_password(self, password: str) -> bool:
        return flask_bcrypt.check_password_hash(self.password, password)

    @staticmethod
    def encode_auth_token(user_public_id: int) -> bytes:
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                "exp": datetime.datetime.utcnow()
                + datetime.timedelta(days=1, seconds=5),
                "iat": datetime.datetime.utcnow(),
                "sub": user_public_id,
            }
            return jwt.encode(payload, key, algorithm="HS256")
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token: str) -> Union[str, int]:
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return "Token blacklisted. Please log in again."
            else:
                return payload["sub"]
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."
