from base.base_test import BaseTest

class TestFormPage(BaseTest):
    def test_form(self):
        self.base_page.open(self.form_page.PAGE_URL)
        self.form_page.enter_first_name(self.data.FIRST_NAME)
        self.form_page.enter_last_name(self.data.LAST_NAME)
        self.form_page.enter_email(self.data.EMAIL)
        self.form_page.enter_mobile(self.data.MOBILE)
        self.form_page.enter_subject(self.data.SUBJECT)
        self.form_page.enter_file_upload(self.data.FILE_PATH)
        self.form_page.enter_current_address(self.data.CURRENT_ADDRESS)
