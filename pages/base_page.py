import string
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator_type, locator_value):
        return self.driver.find_element(locator_type, locator_value)

    def click(self, locator_type, locator_value):
        self.find_element(locator_type, locator_value).click()

    def input_text(self, locator_type, locator_value, text):
        element = self.find_element(locator_type, locator_value)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator_type, locator_value):
        return self.find_element(locator_type, locator_value).text

    # @staticmethod
    # def generate_random_text(length):
    #     """Generate a random string of given length."""
    #     characters = string.ascii_letters + string.digits  # Allowed characters
    #     return ''.join(random.choice(characters) for _ in range(length))

    @staticmethod
    def generate_random_email(length):
        # Example usage
        characters = string.ascii_letters + string.digits  # Allowed characters
        random_text = ''.join(random.choice(characters) for _ in range(length))
        # Create the email with random text
        del_user_email1 = f"brat{random_text}phuser@yopmail.com"
        return del_user_email1
