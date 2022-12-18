import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart import CartPage
from pages.checkout import CheckoutPage
from pages.login import LoginPage
from pages.products import ProductsPage


class TestCart(unittest.TestCase):

    def setUp(self) -> None:
        option = webdriver.ChromeOptions()
        option.add_argument("--headless")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
        self.driver.get("https://automationexercise.com/")

        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

    def test_multiple_products(self):
        self.login_page.login_with_email_password("seleniumremote@gmail.com", "tester")
        self.products_page.add_product_to_cart("men tshirt")
        self.products_page.add_product_to_cart("unicorn")
        self.cart_page.view_cart()
        self.cart_page.proceed_to_checkout()
        product_prices = self.checkout_page.get_product_prices()
        total_amount = self.checkout_page.get_total_amount()
        self.assertEqual(sum(product_prices), total_amount)

    def test_cart_for_unlogged_user(self):
        self.products_page.add_product_to_cart("unicorn")
        self.cart_page.view_cart()
        self.cart_page.proceed_to_checkout()
        self.cart_page.check_if_popup_appeared()

    def test_10_elements_single_item(self):
        self.login_page.login_with_email_password("seleniumremote@gmail.com", "tester")
        self.products_page.add_products_to_cart("unicorn", 10)
        self.cart_page.view_cart()
        self.cart_page.proceed_to_checkout()
        product_prices = self.checkout_page.get_product_prices()
        total_amount = self.checkout_page.get_total_amount()
        self.assertEqual(sum(product_prices), total_amount)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
