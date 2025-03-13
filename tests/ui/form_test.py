from base.base_test import BaseTest
from conftest import driver
class TestFormPage(BaseTest):

    def test_open_url(self):
        self.base_page.open(self.form_page.PAGE_URL)

    def test_field_first_name(self):
        self.form_page.enter_first_name(self.data.FIRST_NAME)

    def test_field_last_name(self):
        self.form_page.enter_last_name(self.data.LAST_NAME)

    def test_gender_radio_button(self):
        self.form_page.click_gender_radio_button()

    def test_field_email(self):
        self.form_page.enter_email(self.data.EMAIL)

    def test_field_mobile(self):
        self.form_page.enter_mobile(self.data.MOBILE)

    def test_field_subject(self):
        self.form_page.enter_subject(self.data.SUBJECT)

    def test_field_file_path(self):
        self.form_page.enter_file_upload(self.data.FILE_PATH)

    def test_hobbies_radio_button(self):
        self.form_page.click_hobbies_radio_button()

    def test_field_current_address(self):
        self.form_page.enter_current_address(self.data.CURRENT_ADDRESS)

    def test_click_button_submit(self):
        self.form_page.click_button_submit()
