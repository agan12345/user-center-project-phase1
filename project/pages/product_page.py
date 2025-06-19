from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/inventory.html"
        self.add_to_cart_button = (By.CLASS_NAME, "btn_inventory")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_badge")
        self.checkout_button = (By.CLASS_NAME, "btn_action")

    def open(self):
        self.driver.get(self.url)

    def add_to_cart(self, product_name):
        product_button = self.driver.find_element(By.XPATH, f"//div[text()='{product_name}']//following-sibling::button")
        product_button.click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_icon).text

    def go_to_cart_and_checkout(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.cart_icon).click()
        self.driver.find_element(*self.checkout_button).click()
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_checkout_success_message(self):
        return self.driver.find_element(By.CLASS_NAME, "complete-header").text
