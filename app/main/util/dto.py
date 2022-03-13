from flask_restx import Namespace, fields


class LogsDto:
    api = Namespace("/access_logs", description="Logs related operations")


class AccessLogsDto:
    api = Namespace("/", description="AccessLog related operations")
    access_log = api.model(
        "access_log_details",
        {
            "path": fields.String(
                required=True, description="path provided by the user"
            ),
            "ip": fields.String(required=True, description="ip from the user"),
            "request_start_time": fields.DateTime(
                required=True, description="Time requested by proxy"
            ),
            "request_end_time": fields.DateTime(
                required=True, description="Response Time"
            ),
            "request": fields.String(required=True, description="request by the user"),
            "response": fields.String(required=True, description="response api"),
            "response_status": fields.String(
                required=True, description="response status by meli api"
            ),
            "method": fields.String(required=True, description="request method"),
        },
    )


class UserDto:
    api = Namespace("user", description="user related operations")

    user = api.model(
        "user",
        {
            "username": fields.String(required=True, description="user username"),
            "email": fields.String(required=True, description="user email address"),
            "password": fields.String(required=True, description="user password"),
        },
    )
    users = api.model(
        "users",
        {
            "username": fields.String(required=True, description="user username"),
            "email": fields.String(required=True, description="user email address"),
            "public_id": fields.Integer(),
            "rol": fields.Integer(),
        },
    )
    update_user = api.model(
        "update_user",
        {
            "username": fields.String(required=True, description="user username"),
            "email": fields.String(description="user email address"),
            "rol": fields.Integer(description="user rol"),
            "password": fields.String(description="user password"),
        },
    )


class ClientDto:
    api = Namespace("client", description="client related operations")
    referrer = api.model(
        "client_referrer",
        {
            "email": fields.String(required=True, description="referrer email"),
            "name": fields.String(required=True, description="referrer name"),
            "phone_number": fields.Integer(
                required=True, description="referrer phone number"
            ),
        },
    )
    address = api.model(
        "client_address",
        {
            "street": fields.String(required=True, description="street name"),
            "number": fields.Integer(required=True, description="street number"),
            "locality": fields.String(required=True, description="locality"),
        },
    )

    client = api.model(
        "client",
        {
            "referrer": fields.Nested(
                referrer, description="contact person of the business"
            ),
            "business_name": fields.String(required=True, description="business name"),
            "address": fields.Nested(address, description="business address"),
            "delivery_man": fields.String(required=True, description="user password"),
        },
    )
    clients = api.model(
        "clients",
        {
            "referrer": fields.Nested(
                referrer, description="contact person of the business"
            ),
            "business_name": fields.String(required=True, description="business name"),
            "address": fields.Nested(address, description="business address"),
            "delivery_man": fields.String(required=True, description="user password"),
        },
    )
    update_client = api.model(
        "update_client",
        {
            "referrer": fields.Nested(
                referrer, description="contact person of the business"
            ),
            "business_name": fields.String(required=True, description="business name"),
            "address": fields.Nested(address, description="business address"),
            "delivery_man": fields.String(required=True, description="user password"),
        },
    )


class ProductDto:
    api = Namespace("product", description="product related operations")
    product = api.model(
        "product",
        {
            "name": fields.String(required=True, description="product name"),
            "max_price": fields.Float(required=True, description="max price"),
            "min_price": fields.Float(required=True, description="min price"),
            "unit_type": fields.String(
                required=True, description="shipment type, for example kg or boxes"
            ),
        },
    )


class SupplierDto:
    api = Namespace("supplier", description="supplier related operations")
    referrer = api.model(
        "supplier_referrer",
        {
            "email": fields.String(required=True, description="referrer email"),
            "name": fields.String(required=True, description="referrer name"),
            "phone_number": fields.Integer(
                required=True, description="referrer phone number"
            ),
        },
    )
    address = api.model(
        "supplier_address",
        {
            "street": fields.String(required=True, description="street name"),
            "number": fields.Integer(required=True, description="street number"),
            "locality": fields.String(required=True, description="locality"),
        },
    )

    supplier = api.model(
        "supplier",
        {
            "referrer": fields.Nested(
                referrer, description="contact person of the business"
            ),
            "business_name": fields.String(required=True, description="business name"),
            "address": fields.Nested(address, description="business address"),
            "delivery_man": fields.String(required=True, description="user password"),
        },
    )

    suppliers = api.model(
        "suppliers",
        {
            "referrer": fields.Nested(
                referrer, description="contact person of the business"
            ),
            "business_name": fields.String(required=True, description="business name"),
            "address": fields.Nested(address, description="business address"),
            "delivery_man": fields.String(required=True, description="user password"),
        },
    )
    update_supplier = api.model(
        "update_supplier",
        {
            "referrer": fields.Nested(
                referrer, description="contact person of the business"
            ),
            "business_name": fields.String(required=True, description="business name"),
            "address": fields.Nested(address, description="business address"),
            "delivery_man": fields.String(required=True, description="user password"),
        },
    )


class StockDto:
    api = Namespace("stock", description="stock related operations")

    payment = api.model(
        "stock_payment",
        {
            "method": fields.String(
                required=True,
                description="payment method, for example: check, transfer, mercadopago, etc..",
            ),
            "total": fields.Float(required=True, description="total to pay"),
            "paid": fields.Float(required=True, description="paid"),
        },
    )

    products = api.model(
        "products",
        {
            "name": fields.String(
                required=True,
                description="product name, for example: fish, another class of fish, etc..",
            ),
            "amount": fields.Integer(required=True, description="amount of product"),
            "amount_type": fields.String(required=True, description="amount type"),
            "price_type": fields.Float(required=True, description="price type"),
        },
    )
    stock = api.model(
        "stock",
        {
            "products": fields.List(fields.Nested(products), description="products"),
            "payment": fields.Nested(
                payment, required=True, description="payment details"
            ),
            "payment_id": fields.Integer(description="payment id"),
            "business_name": fields.String(required=True, description="business name"),
            "entry_type": fields.String(required=True, description="Type of entry"),
            "public_id": fields.Integer(description="publid id"),
            "registered_by": fields.String(description="who created this entry"),
            "registered_on": fields.DateTime(description="when was the entry created"),
        },
    )
    update_stock = api.model(
        "update_stock",
        {
            "products": fields.List(fields.Nested(products), description="products"),
            "payment": fields.Nested(
                payment, required=True, description="payment details"
            ),
            "payment_id": fields.Integer(description="payment id"),
            "business_name": fields.String(required=True, description="business name"),
            "entry_type": fields.String(required=True, description="Type of entry"),
            "public_id": fields.Integer(description="publid id"),
            "registered_by": fields.String(description="who created this entry"),
            "registered_on": fields.DateTime(description="when was the entry created"),
        },
    )


class AuthDto:
    api = Namespace("auth", description="authentication related operations")
    user_auth = api.model(
        "auth_details",
        {
            "username": fields.String(required=True, description="The user name"),
            "password": fields.String(required=True, description="The user password "),
        },
    )


class DeliveryManDto:
    api = Namespace("delivery_man", description="delivery-man related operations")

    delivery_man = api.model(
        "delivery_man",
        {
            "full_name": fields.String(required=True, description="Full name"),
            "short_name": fields.String(required=True, description="Alias"),
            "email": fields.String(required=True, description="business address"),
            "phone_number": fields.Integer(required=True, description="user password"),
            "public_id": fields.Integer(description="user password"),
        },
    )
    delivery_men = api.model(
        "delivery_men",
        {
            "full_name": fields.String(required=True, description="Full name"),
            "short_name": fields.String(required=True, description="Alias"),
            "email": fields.String(required=True, description="business address"),
            "phone_number": fields.Integer(required=True, description="user password"),
            "public_id": fields.Integer(required=True, description="public id'"),
        },
    )


class PingDto:
    api = Namespace("ping", description="health checker")


class CashDto:
    api = Namespace("cash", description="cash related operations")

    payment = api.model(
        "payment",
        {
            "method": fields.String(
                required=True,
                description="payment method, for example: check, transfer, mercadopago, etc..",
            ),
            "total": fields.Float(required=True, description="total to pay"),
            "paid": fields.Float(required=True, description="paid"),
        },
    )

    record = api.model(
        "record",
        {
            "payment": fields.Nested(
                payment, required=True, description="payment details"
            ),
            "reason": fields.String(required=True, description="reason"),
            "destiny": fields.String(required=True, description="origin"),
            "origin": fields.String(required=True, description="origin"),
            "entry_type": fields.String(required=True, description="Type of record"),
            "public_id": fields.Integer(description="public id"),
            "registered_by": fields.String(description="who created this entry"),
            "registered_on": fields.DateTime(description="when was the entry created"),
        },
    )

    records = api.model(
        "records",
        {
            "payment": fields.Nested(payment, description="payment details"),
            "reason": fields.String(description="reason"),
            "destiny": fields.String(description="destiny"),
            "origin": fields.String(description="origin"),
            "entry_type": fields.String(description="Type of record"),
            "public_id": fields.Integer(description="public id"),
            "registered_by": fields.String(description="who created this entry"),
            "registered_on": fields.DateTime(description="when was the entry created"),
        },
    )

    update_record = api.model(
        "records",
        {
            "payment": fields.Nested(
                payment, required=True, description="payment details"
            ),
            "reason": fields.String(required=True, description="reason"),
            "destiny": fields.String(required=True, description="destiny"),
            "origin": fields.String(required=True, description="origin"),
            "entry_type": fields.Boolean(required=True, description="Type of record"),
            "public_id": fields.Integer(description="public id"),
            "registered_by": fields.String(description="who created this entry"),
            "registered_on": fields.DateTime(description="when was the entry created"),
        },
    )
