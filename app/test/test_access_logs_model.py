import unittest

import datetime

from app.main import db
from app.main.model.access_logs import AccessLogs
from app.test.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def test_access_logs_model(self):
        access_log = AccessLogs(
            path='/sites/',
            ip='122.051.2.405',
            time_started=datetime.datetime.now(),
            time_finished=datetime.datetime.now() + datetime.timedelta(0,0.3),
            request=str({"sarasa":"sarasa"}),
            response=str({"sarasa":"sarasa"}),
            response_status = 200,
            method = "get"
        )

        db.session.add(access_log)
        db.session.commit()
        self.assertTrue(True)



if __name__ == '__main__':
    unittest.main()

