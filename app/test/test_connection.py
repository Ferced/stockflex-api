import unittest
from manage import app
from app.main import db
import json
from app.test.base import BaseTestCase
from app.main.model.access_logs_model import AccessLog
import datetime
import redis


def access_meli_api(self):
    return self.client.get(
        "/sites/",
    )


class TestAccessBlueprint(BaseTestCase):
    def test_connection_meli_api(self):
        """Test for connection to meli api"""
        with self.client:
            response = access_meli_api(self)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

    def test_connection_mongodb(self):
        """Test for connection to meli api"""
        access_log = AccessLog(
            path="/sites/",
            ip="122.051.2.405",
            request_start_time=datetime.datetime.now(),
            request_end_time=datetime.datetime.now() + datetime.timedelta(0, 0.3),
            request=str({"sarasa": "sarasa"}),
            response=str({"sarasa": "sarasa"}),
            response_status=200,
            method="GET",
        )
        access_log.save()
        self.assertTrue(True)

    def test_connection_redis(self):
        """Test for connection to meli api"""
        cache_log_path = "/sites/"
        cache_log_limit = 10
        redis_client = redis.Redis(
            host=app.config["REDIS_HOST"], port=app.config["REDIS_PORT"]
        )
        redis_client.set(cache_log_path, cache_log_limit)
        self.assertTrue(int(redis_client.get(cache_log_path)) == cache_log_limit)


if __name__ == "__main__":
    unittest.main()
