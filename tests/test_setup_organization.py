import pytest
from pages.base_page import BasePage
from pages.setup_organization import SetupOrganizationPage
from config.config import Config
from pages.signup_page import SignupPage


# @pytest.mark.order(2)
def test_setup_organization(driver):
    signup_page = SignupPage(driver)
    signup_page.open_url("https://app.indev.proofhub.com/api/v5/ph_backend_stage/public/oauth/signup")
    email_random1 = BasePage.generate_random_email(10)
    signup_page.signup(email_random1, email_random1)
    setup_organization_page = SetupOrganizationPage(driver)
    setup_organization_page.setup_organization("Pycharm_org", "Pycharm_work")
    # basepage = BasePage(driver)

    title_setup_workspace = driver.get_text("xpath", "//*[@id='app']/div/div/div/div/div/div[2]/div/h2")
    assert title_setup_workspace == "Setup your workspace", "SignUp Failed"
