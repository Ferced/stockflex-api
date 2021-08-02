import uuid
import datetime
import requests
from app.main import db
from app.main.model.access_logs import AccessLogs
from app.main.helpers.constants.constants_general import ConstantsGeneral
from typing import Dict, Tuple

class AccessService():
    @staticmethod
    def get_new_access(data,path,ip,method):
        try:
            time_request_start = datetime.datetime.now()
            response_object,response_status =  AccessService.get_meli_api(path,data,method)

            new_access_log = AccessLogs(
                path = path,
                ip = ip,
                time_started = time_request_start,
                time_finished = datetime.datetime.now(),
                request = str(data),
                response = str(response_object),
                response_status = response_status,
                method=method
            )
            
            AccessService.save_changes(new_access_log) 
            return response_object,response_status

        except Exception as e:
            response_status = 500
            response_object = {
                'message': 'internal proxy error',
                'error':e,
                'status': response_status,
            }
            return response_object, response_status

    @staticmethod
    def get_meli_api(path,data,method):
        url = ConstantsGeneral.url_api_meli+path
        params = data
        resp = requests.request(method,url=url,params=params)
        response_object = resp.json()
        return response_object,resp.status_code
    
    @staticmethod
    def save_changes(data: AccessLogs) -> None:
        db.session.add(data)
        db.session.commit()

