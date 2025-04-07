from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import random
# import string
#
#
# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def open_url(self, url):
#         self.driver.get(url)
#
#     def find_element(self, locator_type, locator_value):
#         return self.driver.find_element(locator_type, locator_value)
#
#     def click(self, locator_type, locator_value):
#         self.find_element(locator_type, locator_value).click()
#
#     def input_text(self, locator_type, locator_value, text):
#         element = self.find_element(locator_type, locator_value)
#         element.clear()
#         element.send_keys(text)
#
#     def get_text(self, locator_type, locator_value):
#         return self.find_element(locator_type, locator_value).text
#
#     def generate_random_text(self, length):
#         """Generate a random string of given length."""
#         characters = string.ascii_letters + string.digits  # Allowed characters
#         return ''.join(random.choice(characters) for _ in range(length))
#
#     # @staticmethod
#     def generate_random_email(self):
#         # Example usage
#         random_text = self.generate_random_text(10)  # Generates a random string of 10 characters
#         # Create the email with random text
#         del_user_email1 = f"brat{random_text}phuser@yopmail.com"
#         return del_user_email1
