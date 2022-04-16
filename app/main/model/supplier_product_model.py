from enum import unique
from .. import db


class SupplierProduct(db.Document):
    name = db.StringField(required=True)
    price = db.DecimalField(required=True)
    supplier_name = db.StringField(required=True)
    unit_type = db.StringField(required=True)
    public_id = db.IntField(required=True, unique=True)
    registered_by = db.StringField(required=True)
    registered_on = db.DateTimeField(required=True)

    def to_json(self):
        return {
            "name": self.name,
            "price": self.price,
            "supplier_name": self.supplier_name,
            "unit_type": self.unit_type,
            "public_id": self.public_id,
            "registered_by": self.registered_by,
            "registered_on": self.registered_on,
        }
