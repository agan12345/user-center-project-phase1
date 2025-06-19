from selenium.webdriver.common.by import By

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_button = (By.ID, "logout_sidebar_link")
        self.login_title = (By.CLASS_NAME, "login_logo")

    def open_menu(self):
        self.driver.find_element(*self.menu_button).click()

    def logout(self):
        self.open_menu()
        self.driver.find_element(*self.logout_button).click()

    def login(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    def is_login_successful(self):
        return "inventory" in self.driver.current_url
