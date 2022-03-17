import uuid
from datetime import datetime, timedelta
from app.main.model.stock_model import Stock
from app.main.model.cash_model import Cash
from app.main.model.supplier_model import Supplier
from app.main.model.client_model import Client
from app.main.helpers.auth_helper import Auth
from dateutil import parser
import ast


def save_new_record(data, user):
    try:
        public_id = int(uuid.uuid4().int >> 100)
        new_record = Cash(
            payment=data["payment"],
            origin=data["payment"]["method"]
            if data["entry_type"] == "deposito"
            else data["business_name"],
            destiny=data["business_name"]
            if data["entry_type"] == "deposito"
            else data["payment"]["method"],
            reason="stock",
            entry_type=data["entry_type"],
            public_id=public_id,
            registered_by=user["username"],
            registered_on=datetime.utcnow(),
        )
        new_record.save()
        return public_id

    except Exception as e:
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
            "description": str(e),
        }
        return response_object, 500


def save_new_stock(request):
    try:
        user = Auth.get_username_by_token(request.headers["Authorization"])
        data = request.get_json()
        try:
            if data["entry_type"] == "pago":
                business = Supplier.objects(business_name=data["business_name"]).first()
                print("BUSINESS: ", business)
            else:
                business = Client.objects(business_name=data["business_name"]).first()
            if business:
                new_stock = Stock(
                    products=data["products"],
                    payment_id=save_new_record(data, user),
                    business_name=data["business_name"],
                    entry_type=data["entry_type"],
                    public_id=int(uuid.uuid4().int >> 100),
                    registered_by=user["username"],
                    registered_on=datetime.utcnow(),
                )
                new_stock.save()

            else:
                response_object = {
                    "status": "fail",
                    "message": "Supplier not registered.",
                }
                return response_object, 409
            response_object = {
                "status": "success",
                "message": "Successfully saved.",
            }
            return response_object, 200
        except Exception as e:
            print(e)
            response_object = {
                "status": "fail",
                "message": "Some error occurred. Please try again.",
                "description": str(e),
            }
            return response_object, 500
    except Exception as e:
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
            "description": str(e),
        }
        return response_object, 500


def get_all_stocks(request):
    try:
        data = request.args.to_dict()
        if "registered_on" in data:
            date_from = datetime.strptime(data["registered_on"], "%d/%m/%Y")
            date_to = datetime.strptime(data["registered_on"], "%d/%m/%Y") + timedelta(
                days=1
            )
            data["registered_on__gte"] = date_from.strftime("%Y-%-m-%-d %H:%M:%S")
            data["registered_on__lte"] = date_to.strftime("%Y-%-m-%-d %H:%M:%S")
            del data["registered_on"]

        data = ast.literal_eval(str(data).replace("[", "__").replace("]", ""))
        # all_stocks = [stock for stock in Stock.objects(**data)]
        all_stocks = [stock for stock in Stock.objects.filter(**data)]

        stocks_with_payment = []
        for stock in all_stocks:
            stock_json = stock.to_json()
            stock_json["payment"] = Cash.objects(public_id=stock.payment_id)[
                0
            ].to_json()["payment"]
            stocks_with_payment.append(stock_json)
        return stocks_with_payment, 200
    except Exception as e:
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
            "description": str(e),
        }
        return response_object, 500


def update_stock(data):
    try:
        payment_data = {"payment": data["payment"]}
        del data["registered_on"]
        del data["registered_by"]
        try:
            # print("DATA RECEIBED: ", data)
            cash_to_update = Cash.objects(public_id=data["payment_id"]).first()
            cash_to_update.update(**payment_data)
            cash_to_update.save()
            del data["payment"]
            del data["payment_id"]
            stock_to_update = Stock.objects(public_id=data["public_id"]).first()
            del data["public_id"]
            stock_to_update.update(**data)
            stock_to_update.save()
            response_object = {"status": "success", "message": "Successfully updated."}
            return response_object, 200
        except Exception as e:
            print(e)
            response_object = {
                "status": "fail",
                "message": "Some error occurred. Please try again.",
                "description": str(e),
            }
            return response_object, 500
    except Exception as e:
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
            "description": str(e),
        }
        return response_object, 500


def delete_stock(request):
    try:
        stock_to_delete = Stock.objects(**request.args).first()
        stock_to_delete.delete()
        response_object = {"status": "success", "message": "Successfully deleted."}
        return response_object, 200

    except Exception as e:
        print(e)
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
            "description": str(e),
        }
        return response_object, 500
