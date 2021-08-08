import uuid
import datetime
import requests
from http import HTTPStatus
from app.main import db
from app.main.model.access_logs_model import AccessLog
from app.main.helpers.constants.constants_general import GeneralConstants
from typing import Dict, Tuple


class ProxyService:
    @staticmethod
    def forward_request(path, data, method, access_token):

        url = GeneralConstants.url_api_meli + path
        params = data
        resp = requests.request(
            method,
            url=url,
            params=params,
            headers={"Authorization": "Bearer " + access_token},
        )
        response_object = resp.json()
        return response_object, resp.status_code

    @staticmethod
    def handle_request(request):
        try:
            path = request.full_path
            data = request.json
            ip = request.remote_addr
            method = request.method
            access_token = str(request.headers.get("Authorization"))
            request_start_time = datetime.datetime.now()
            response_object, response_status = ProxyService.forward_request(
                path,
                data,
                method,
                access_token,
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

            access_log.save()
            return response_object, response_status

        except Exception as e:
            response_status = HTTPStatus.INTERNAL_SERVER_ERROR
            response_object = {
                "message": "internal error",
                "error": e,
                "status": response_status,
            }
            return response_object, response_status
