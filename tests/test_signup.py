import pytest
from pages.base_page import BasePage
from pages.signup_page import SignupPage
from config.config import Config


def test_signup(driver):
    signup_page = SignupPage(driver)
    signup_page.open_url("https://app.indev.proofhub.com/api/v5/ph_backend_stage/public/oauth/signup")
    email_random = BasePage.generate_random_email(10)
    # print(email_random)
    signup_page.signup(email_random, email_random)
    # ✅ Assertion: Verify signup success message
    success_message = signup_page.get_text("xpath", "//*[@id='app']/div/div/div/div/div/div[2]/div/h2")
    assert "Setup your workspace" in success_message, "Signup failed!"


def test_signup_existing_email(driver):
    signup_page = SignupPage(driver)
    signup_page.open_url("https://app.indev.proofhub.com/api/v5/ph_backend_stage/public/oauth/signup")
    signup_page.signup("cathy.t.mathews@gmail.com", "testing12345")
    # ✅ Assertion: Verify signup success message
    success_message = signup_page.get_text("xpath", "//*[@id='app']/div/div/div/div/div/div[2]/div/div/h2")
    assert "Choose your workspace" in success_message, "Signup failed!"

