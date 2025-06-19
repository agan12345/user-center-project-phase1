from project.pages.logout_page import LogoutPage

def test_logout_success(driver):
    page = LogoutPage(driver)
    page.login()  # 登录
    page.logout()  # 退出
    assert "saucedemo.com" in driver.current_url

def test_login_persist_after_refresh(driver):
    page = LogoutPage(driver)
    page.login()
    driver.refresh()
    assert page.is_login_successful()
