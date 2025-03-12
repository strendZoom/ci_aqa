import pytest
from locators.data import Data
from pages.form_page import FormPage
from base.base_page import BasePage

class BaseTest:
    form_page : FormPage
    base_page : BasePage
    data : Data

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.form_page = FormPage(driver)
        request.cls.base_page = BasePage(driver)