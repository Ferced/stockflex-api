from .. import db


class Products(db.EmbeddedDocument):
    name = db.StringField(required=True)
    amount = db.DecimalField(required=True)
    amount_type = db.StringField(required=True)
    price_type = db.DecimalField(required=True)

    def to_json(self):
        return {
            "name": self.name,
            "amount": self.amount,
            "amount_type": self.amount_type,
            "price_type": self.price_type,
        }


class Stock(db.Document):
    products = db.ListField(db.EmbeddedDocumentField(Products), required=True)
    payment_id = db.IntField(required=True, unique=True)
    business_name = db.StringField(required=True)
    public_id = db.IntField(required=True, unique=True)
    entry_type = db.StringField(required=True)
    registered_by = db.StringField(required=True)
    registered_on = db.DateTimeField(required=True)

    def to_json(self):
        return {
            "products": self.products,
            "payment_id": self.payment_id,
            "business_name": self.business_name,
            "public_id": self.public_id,
            "entry_type": self.entry_type,
            "registered_by": self.registered_by,
            "registered_on": self.registered_on,
        }
