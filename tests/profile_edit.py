from pages.base_page import BasePage
from config.config import Config
def test_profile_edit(setup):
    driver = setup
    driver.get(Config.BASE_URL + "/profile")
    profile_page = ProfilePage(driver)
    profile_page.edit_profile("New Name")
    assert "New Name" in driver.page_source

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# tests/test_profile.py
import pytest
from pages.profile_page import ProfilePage

@pytest.mark.order(5)
def test_edit_profile(browser):
    profile_page = ProfilePage(browser)
    profile_page.edit_profile("New Name")
    assert profile_page.get_profile_name() == "New Name"

