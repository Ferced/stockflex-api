from datetime import datetime, timedelta

# from .. import redis_client
import json
from app.main.helpers.constants.constants_general import LimiterConstants


class RateLimit:
    @staticmethod
    def is_ip_allowed(ip):
        limit = LimiterConstants.ip_limit
        period = timedelta(seconds=LimiterConstants.ip_limit_period)
        return RateLimit.request_is_not_limited(redis_client, ip, limit, period)

    @staticmethod
    def is_path_allowed(path):
        limit = LimiterConstants.path_limit
        period = timedelta(seconds=LimiterConstants.path_limit_period)
        return RateLimit.request_is_not_limited(redis_client, path, limit, period)

    @staticmethod
    def is_combo_allowed(key1, key2):
        limit = LimiterConstants.combo_limit
        period = timedelta(seconds=LimiterConstants.combo_limit_period)
        key = f"{key1}:{key2}"
        return RateLimit.request_is_not_limited(redis_client, key, limit, period)

    @staticmethod
    def request_is_not_limited(redis_client, redis_key, redis_limit, redis_period):
        if redis_client.setnx(redis_key, redis_limit):
            redis_client.expire(redis_key, int(redis_period.total_seconds()))
        remaining_requests = redis_client.get(redis_key)
        if remaining_requests and int(remaining_requests) > 0:
            redis_client.decrby(redis_key, 1)
            return True
        return False

    @staticmethod
    def is_blacklisted(redis_client, redis_key):

        redis_client.rpush("blacklist_ip", redis_key)
        # if Connections.redis_client.setnx(redis_key, redis_limit):
        #     Connections.redis_client.expire(redis_key, int(redis_period.total_seconds()))

        remaining_requests = redis_client.get(redis_key)
        if remaining_requests and int(remaining_requests) > 0:
            redis_client.decrby(redis_key, 1)
            return True

        return False
