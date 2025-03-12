from selenium.webdriver.common.by import By
from locators.links import Links
from base.base_page import BasePage
from selenium.webdriver import Keys
from random import randint
from selenium.webdriver.support import expected_conditions as EC
import logging
logging.basicConfig(level=logging.INFO)

class FormPage(BasePage):
    PAGE_URL = Links.FORM_PAGE
    LAST_NAME = (By.CSS_SELECTOR, '#lastName')
    FIRST_NAME = (By.CSS_SELECTOR, '#firstName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    GENDER = (By.XPATH, f'//*[@for="gender-radio-{randint(1, 3)}"]')
    MOBILE = (By.CSS_SELECTOR, "#userNumber")
    SUBJECT = (By.CSS_SELECTOR, "#subjectsInput")
    HOBBIES = (By.XPATH, f'//*[@for="hobbies-checkbox-{randint(1, 3)}"]')
    FILE_INPUT = (By.CSS_SELECTOR, "#uploadPicture")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")
    SUBMIT = (By.CSS_SELECTOR, "#submit")
    RESULT_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')


    def enter_first_name(self,data):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME)).send_keys(data)
        logging.info(f"Заполнено поле: {self.FIRST_NAME}, значением: {data}")

    def enter_last_name(self,data):
        self.wait.until(EC.element_to_be_clickable(self.LAST_NAME)).send_keys(data)
        logging.info(f"Заполнено поле: {self.LAST_NAME}, значением: {data}")

    def enter_email(self,data):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL)).send_keys(data)
        logging.info(f"Заполнено поле: {self.EMAIL}, значением: {data}")

    def enter_mobile(self,data):
        self.wait.until(EC.element_to_be_clickable(self.MOBILE)).send_keys(data)
        logging.info(f"Заполнено поле: {self.MOBILE}, значением: {data}")

    def enter_subject(self,data):
        subject = self.wait.until(EC.element_to_be_clickable(self.SUBJECT))
        subject.send_keys(data)
        subject.send_keys(Keys.RETURN)
        logging.info(f"Заполнено поле: {self.SUBJECT}, значением: {data}")

    def enter_file_upload(self,data):
        self.wait.until(EC.element_to_be_clickable(self.FILE_INPUT)).send_keys(data)
        logging.info(f"Заполнено поле: {self.FILE_INPUT}, значением: {data}")

    def enter_current_address(self, data):
        self.wait.until(EC.element_to_be_clickable(self.CURRENT_ADDRESS)).send_keys(data)
        logging.info(f"Заполнено поле: {self.CURRENT_ADDRESS}, значением: {data }")

    def click_gender_radio_button(self):
        self.wait.until(EC.element_to_be_clickable(self.GENDER)).click()
        logging.info(f"Поле {self.GENDER} клик")

    def click_hobbies_radio_button(self):
        self.wait.until(EC.element_to_be_clickable(self.HOBBIES)).click()

    def click_button_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT)).click()