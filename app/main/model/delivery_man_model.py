from .. import db


class DeliveryMan(db.Document):
    full_name = db.StringField(required=True, unique=True)
    short_name = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    phone_number = db.IntField(max_length=30, required=True, unique=True)
    public_id = db.IntField(required=True, unique=True)
    registered_on = db.DateTimeField(required=True)

    def to_json(self):
        return {
            "full_name": self.full_name,
            "short_name": self.short_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "public_id": self.public_id,
            "registered_on": self.registered_on,
        }
