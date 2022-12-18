import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.login import LoginPage
from pages.products import ProductsPage


class TestCart(unittest.TestCase):
    cart_tab_selector = (By.XPATH, "//*[@href='/view_cart']")
    checkout_button_selector = (By.CLASS_NAME, "check_out")
    cart_price_selector = (By.CLASS_NAME, "cart_total_price")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://automationexercise.com/")

        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)

        self.login_page.login_with_email_password("seleniumremote@gmail.com", "tester")

    def test_multiple_products(self):
        self.products_page.add_product_to_cart("men tshirt")
        self.products_page.add_product_to_cart("unicorn")

        self.driver.find_element(*self.cart_tab_selector).click()
        self.driver.find_element(*self.checkout_button_selector).click()

        prices_elements = self.driver.find_elements(*self.cart_price_selector)

        sum_prices = 0
        for price_element in prices_elements[:-1]:
            sum_prices += int(price_element.text[3:])

        total_amount = int(prices_elements[-1].text[3:])

        self.assertEqual(sum_prices, total_amount)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
