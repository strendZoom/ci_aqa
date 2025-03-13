import pytest
from locators.data import Data
from pages.form_page import FormPage
from base.base_page import BasePage
from pages.auth_page import AuthPage
from tests.api.clients.user_client import UserClient

class BaseTest:
    form_page : FormPage
    base_page : BasePage
    auth_page : AuthPage
    user_client : UserClient
    data : Data

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.form_page = FormPage(driver)
        request.cls.base_page = BasePage(driver)
        request.cls.auth_page = AuthPage(driver)
        request.cls.user_client = UserClient(driver)