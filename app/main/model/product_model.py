from enum import unique
from .. import db


class Product(db.Document):
    name = db.StringField(required=True, unique=True)
    min_price = db.DecimalField(required=True)
    max_price = db.DecimalField(required=True)
    unit_type = db.StringField(required=True)
    public_id = db.IntField(required=True, unique=True)
    registered_by = db.StringField(required=True)
    registered_on = db.DateTimeField(required=True)

    def to_json(self):
        return {
            "name": self.name,
            "min_price": self.min_price,
            "max_price": self.max_price,
            "public_id": self.public_id,
            "unit_type": self.unit_type,
            "registered_by": self.registered_by,
            "registered_on": self.registered_on,
        }
