import unittest

from app.main import db
import json
from app.test.base import BaseTestCase


def get_access_logs(self, path):
    return self.client.get(
        path,
    )


class TestAccessBlueprint(BaseTestCase):
    def test_connection_proxy_logs(self):
        """Test for connection to access logs"""
        with self.client:
            response = get_access_logs(self, "/proxy/access_logs/")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

    def test_connection_proxy_logs_path_count(self):
        """Test for connection to access logs"""
        with self.client:
            response = get_access_logs(self, "/proxy/access_logs/path_count/")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

    def test_connection_proxy_logs_method_count(self):
        """Test for connection to access logs"""
        with self.client:
            response = get_access_logs(self, "/proxy/access_logs/method_count/")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
