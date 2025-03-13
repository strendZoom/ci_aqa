import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10,1)

    def open(self, url):
        self.driver.get(url)

    def is_opened(self,url):
        self.wait.until(EC.url_to_be(url))

    # def make_screenshot(self, screenshot_name):
    #     allure.attach(
    #         body=self.driver.get_screenshot_as_png(),
    #         name=screenshot_name,
    #         attachment_type=AttachmentType.PNG)