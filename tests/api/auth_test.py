import unittest
from schemas.user_schema import TokenSchema, UserSchema
from locators.data import Data
from tests.api.clients.user_client import UserClient

class TestApiAuth(unittest.TestCase):

    def test_auth(self):
        client = UserClient()
        token = client.generate_token(data={"userName": Data.OLD_USER_LOGIN, "password": Data.OLD_USER_PASSWORD})
        self.assertEqual(token.status_code, 200)
        self.assertTrue(len(token.json()) > 0)
        token = token.json()
        TokenSchema(**token)
        auth =  client.login(data={"userName": Data.OLD_USER_LOGIN,"password": Data.OLD_USER_PASSWORD})
        user_data = auth.json()
        UserSchema(**user_data)