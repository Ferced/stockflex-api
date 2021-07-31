from datetime import datetime,timedelta

from app.main.model.products import Products
from app.main.helpers.constants.constants_general import ConstantsLimiter
from typing import Dict, Tuple


class Limiter:
    @staticmethod
    def ip_limiter(request):
        try:
            # fetch the products data
            products = Products.query.filter(Products.ip==request.remote_addr,Products.time_finished >= datetime.now() - timedelta(hours=1) ).all()
            if len(products)>ConstantsLimiter.ip_limit_per_hour:
                response_object = {
                    'status': 'fail',
                    'message': 'Too many re quests'
                }
                return response_object, 429
            else:
                response_object = {
                    'status': 'success',
                    'message': 'success'
                }
                return response_object, 200
        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Internal proxy error'
            }
            return response_object, 500


    @staticmethod
    def path_limiter(request):
        try:
            # fetch the products data
            products = Products.query.filter_by(path=request.path[1:]).all()
            if len(products)>ConstantsLimiter.path_limit_per_hour:
                response_object = {
                    'status': 'fail', 
                    'message': 'Too many requests'
                }
                return response_object, 429
            else:
                response_object = {
                    'status': 'success',
                    'message': 'success'
                }
                return response_object, 200
        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Internal proxy error'
            }
            return response_object, 500

