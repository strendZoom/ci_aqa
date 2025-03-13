from selenium.webdriver.common.by import By
from locators.links import Links
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import logging
logging.basicConfig(level=logging.INFO)

class AuthPage(BasePage):
    PAGE_URL = Links.AUTH_PAGE
    LOGIN = (By.CSS_SELECTOR, '#userName')
    USER_PASSWORD = (By.CSS_SELECTOR, "#password")
    SUBMIT = (By.CSS_SELECTOR, "#login")

    def enter_login(self,data):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN)).send_keys(data)
        logging.info(f"Заполнено поле: {self.LOGIN}, значением: {data}")

    def enter_password(self,data):
        self.wait.until(EC.element_to_be_clickable(self.USER_PASSWORD)).send_keys(data)
        logging.info(f"Заполнено поле: {self.USER_PASSWORD}, значением: {data}")

    def click_button_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT)).click()