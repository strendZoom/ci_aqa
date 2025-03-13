import os
from dotenv import load_dotenv
load_dotenv()

class Data:
    FIRST_NAME = os.getenv("FIRST_NAME")
    LAST_NAME = os.getenv("LAST_NAME")
    EMAIL = os.getenv("EMAIL")
    MOBILE = os.getenv("MOBILE")
    SUBJECT = os.getenv("SUBJECT")
    FILE_PATH = os.getenv("FILE_PATH")
    CURRENT_ADDRESS = os.getenv("CURRENT_ADDRESS")
    OLD_USER_LOGIN = os.getenv("OLD_USER_LOGIN")
    OLD_USER_PASSWORD = os.getenv("OLD_USER_PASSWORD")