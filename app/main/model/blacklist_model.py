from .. import db
import datetime


class BlacklistToken(db.Document):
    """
    Token Model for storing JWT tokens
    """

    token = db.StringField()
    blacklisted_on = db.DateTimeField()

    def clean(self):
        self.blacklisted_on = datetime.datetime.now()

    @staticmethod
    def check_blacklist(auth_token: str) -> bool:
        # check whether auth token has been blacklisted
        res = BlacklistToken.objects(token=str(auth_token)).first()
        if res:
            return True
        else:
            return False
