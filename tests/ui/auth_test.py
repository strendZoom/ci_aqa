from base.base_test import BaseTest
from conftest import driver

class TestAuthPage(BaseTest):

    def test_open_url(self):
        self.base_page.open(self.auth_page.PAGE_URL)

    def test_field_login(self):
        self.auth_page.enter_login(self.data.OLD_USER_LOGIN)

    def test_field_password(self):
        self.auth_page.enter_password(self.data.OLD_USER_PASSWORD)

    def test_click_button_submit(self):
        self.auth_page.click_button_submit()
