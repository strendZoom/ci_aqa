import unittest
from schemas.user_schema import TokenSchema, UserSchema
from locators.data import Data
from tests.api.clients.user_client import UserClient
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestApiAuth(unittest.TestCase):

    def test_generate_token(self):
        client = UserClient()
        resp = client.generate_token(data={"userName": Data.OLD_USER_LOGIN, "password": Data.OLD_USER_PASSWORD})
        self.assertEqual(resp.status_code, 200)
        body = resp.json()
        TokenSchema(**body)
        logger.info(f"Status code {self.assertEqual(resp.status_code, 200)}, {body}, ")


    def test_login(self):
        client = UserClient()
        resp = client.login(data={"userName": Data.OLD_USER_LOGIN, "password": Data.OLD_USER_PASSWORD})
        self.assertEqual(resp.status_code, 200)
        body = resp.json()
        UserSchema(**body)
        logger.info(f"test_login: Status code {self.assertEqual(resp.status_code, 200)}, {body},")
