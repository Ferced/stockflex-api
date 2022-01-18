from .. import db


class Referrer(db.EmbeddedDocument):
    email = db.EmailField(required=True)
    name = db.StringField(max_length=30, required=True)
    phone_number = db.IntField()

    def to_json(self):
        return {
            "email": self.email,
            "name": self.name,
            "phone_number": self.phone_number,
        }


class Address(db.EmbeddedDocument):
    street = db.StringField(required=True)
    number = db.IntField(max_length=30, required=True)
    locality = db.StringField(required=True)

    def to_json(self):
        return {
            "street": self.street,
            "number": self.number,
            "locality": self.locality,
        }


class Supplier(db.Document):
    referrer = db.EmbeddedDocumentField(Referrer, required=True)
    business_name = db.StringField(required=True, unique=True)
    address = db.EmbeddedDocumentField(Address, required=True)
    delivery_man = db.StringField(required=True)
    registered_on = db.DateTimeField(required=True)

    def to_json(self):
        return {
            "referrer": self.referrer.to_json(),
            "business_name": self.business_name,
            "address": self.address.to_json(),
            "delivery_man": self.delivery_man,
        }
