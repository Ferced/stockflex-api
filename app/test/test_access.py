import unittest

from app.main import db
import json
from app.test.base import BaseTestCase


def access_meli_api(self):
    return self.client.get(
        '/sites/',
    )


class TestAccessBlueprint(BaseTestCase):
    def test_connection_meli_api(self):
        """ Test for connectio to meli api"""
        with self.client:
            response = access_meli_api(self)
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
