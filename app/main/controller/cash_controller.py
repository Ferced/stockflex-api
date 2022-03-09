from flask import request
from flask_restx import Resource
from app.main.util.decorator import admin_token_required
from ..util.dto import CashDto
from ..service.cash_service import (
    delete_record,
    save_new_record,
    get_all_records,
    update_record,
    delete_record,
)
from typing import Dict, Tuple

api = CashDto.api
_record = CashDto.record
_records = CashDto.records
_update_record = CashDto.update_record


@api.route("/")
class Cash(Resource):
    @api.doc("list registered records")
    # @admin_token_required
    @api.marshal_list_with(_records, envelope="data")
    def get(self):
        # print(request.headers)
        # print(request.json)
        """List all registered records"""
        return get_all_records(request)

    @api.expect(_record, validate=True)
    @api.response(201, "Cash record successfully created.")
    @admin_token_required
    @api.doc("create a new cash record")
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new cash record"""
        return save_new_record(request)

    # @api.expect(_update_record, validate=True)
    @api.doc("update cash record")
    @admin_token_required
    def put(self):
        """Update cash records"""
        data = request.json
        print("data: ", data)
        return update_record(data)

    # @api.expect(_update_record, validate=True)
    @api.doc("delete cash record")
    @admin_token_required
    def delete(self):
        """delete records"""
        return delete_record(request)
