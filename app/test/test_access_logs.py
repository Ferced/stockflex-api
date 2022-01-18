import unittest

from app.main import db
import json
from app.test.base import BaseTestCase
from manage import app


def get_access_logs(self, path):
    return self.client.get(
        path,
    )


class TestAccessLogsBlueprint(BaseTestCase):
    def test_proxy_logs(self):
        """Test access logs"""
        with self.client:
            response = get_access_logs(self, "/proxy/access_logs/")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

    def test_connection_proxy_logs_path_count(self):
        """Test access logs count"""
        with self.client:
            response = get_access_logs(self, "/proxy/access_logs/count/ip")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

    def test_proxy_logs_params(self):
        """Test f to access logs"""
        with self.client:
            response = get_access_logs(self, "/proxy/access_logs/?method=GET")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
