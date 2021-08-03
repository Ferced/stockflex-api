import uuid
import datetime
import requests
from http import HTTPStatus
from app.main import db
from app.main.model.access_logs import AccessLog
from app.main.helpers.constants.constants_general import GeneralConstants
from typing import Dict, Tuple


class ProxyService:
    @staticmethod
    def handle_request(data, path, ip, method):
        try:
            request_start_time = datetime.datetime.now()
            response_object, response_status = ProxyService.forward_request(
                path, data, method
            )

            access_log = AccessLog(
                path=path,
                ip=ip,
                request_start_time=request_start_time,
                request_end_time=datetime.datetime.now(),
                request=str(data),
                response=str(response_object),
                response_status=response_status,
                method=method,
            )

            ProxyService.store(access_log)
            return response_object, response_status

        except Exception as e:
            response_status = HTTPStatus.INTERNAL_SERVER_ERROR
            response_object = {
                "message": "internal error",
                "error": e,
                "status": response_status,
            }
            return response_object, response_status

    @staticmethod
    def forward_request(path, data, method):
        url = GeneralConstants.url_api_meli + path
        params = data
        resp = requests.request(method, url=url, params=params)
        response_object = resp.json()
        return response_object, resp.status_code

    @staticmethod
    def store(data: AccessLog) -> None:
        db.session.add(data)
        db.session.commit()
