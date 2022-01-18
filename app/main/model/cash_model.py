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


class Cash(db.Document):
    payment = db.EmbeddedDocumentField(Payment, required=True)
    origin = db.StringField(required=True)
    destiny = db.StringField(required=True)
    reason = db.StringField(required=True)
    type = db.StringField(required=True)
    public_id = db.IntField(required=True, unique=True)
    registered_by = db.StringField(required=True)
    registered_on = db.DateTimeField(required=True)

    def to_json(self):
        return {
            "payment": self.payment.to_json(),
            "origin": self.origin,
            "destiny": self.destiny,
            "reason": self.reason,
            "type": self.type,
            "public_id": self.public_id,
            "registered_by": self.registered_by,
            "registered_on": self.registered_on,
        }
