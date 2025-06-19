from project.pages.product_page import ProductPage

def test_add_one_product_to_cart(driver):
    product_page = ProductPage(driver)
    product_page.open()
    product_page.add_to_cart("Sauce Labs Backpack")
    assert product_page.get_cart_count() == "1"

def test_checkout_two_products(driver):
    product_page = ProductPage(driver)
    product_page.open()
    product_page.add_to_cart("Sauce Labs Backpack")
    product_page.add_to_cart("Sauce Labs Bike Light")
    product_page.go_to_cart_and_checkout("John", "Smith", "12345")
    assert product_page.get_checkout_success_message() == "Thank you for your order!"
