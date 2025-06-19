import pytest
from project.pages.login_page import LoginPage

def test_login_success(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    assert page.is_login_successful()

def test_login_fail_wrong_password(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "wrong_password")
    assert "Epic sadface" in page.get_error_message()
