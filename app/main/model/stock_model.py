from .. import db


class Payment(db.EmbeddedDocument):
    method = db.StringField(required=True)
    total = db.DecimalField(required=True)
    paid = db.DecimalField(required=True)

    def to_json(self):
        return {
            "method": self.method,
            "total": self.total,
            "paid": self.paid,
        }


class Stock(db.Document):
    product_name = db.StringField(required=True)
    amount = db.DecimalField(required=True)
    amount_type = db.StringField(required=True)
    payment = db.EmbeddedDocumentField(Payment, required=True)
    business_name = db.StringField(required=True)
    public_id = db.IntField(required=True, unique=True)
    entry_type = db.BooleanField(required=True)
    registered_by = db.StringField(required=True)
    registered_on = db.DateTimeField(required=True)

    def to_json(self):
        return {
            "product_name": self.product_name,
            "amount": self.amount,
            "amount_type": self.amount_type,
            "payment": self.payment.to_json(),
            "business_name": self.business_name,
            "public_id": self.public_id,
            "entry_type": self.entry_type,
            "registered_by": self.registered_by,
            "registered_on": self.registered_on,
        }
