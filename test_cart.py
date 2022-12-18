import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class TestCart(unittest.TestCase):

    login_tab_selector = (By.CSS_SELECTOR, "a[href='/login']")
    email_field_selector = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    password_field_selector = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    login_button_selector = (By.CSS_SELECTOR, "button[data-qa='login-button']")

    products_tab_selector = (By.XPATH, "//*[@href='/products']")
    search_product_field_selector = (By.ID, "search_product")
    add_to_cart_button_selector = (By.CLASS_NAME, "add-to-cart")
    continue_shopping_button_selector = (By.CLASS_NAME, "close-modal")
    cart_tab_selector = (By.XPATH, "//*[@href='/view_cart']")
    checkout_button_selector = (By.CLASS_NAME, "check_out")
    cart_price_selector = (By.CLASS_NAME, "cart_total_price")

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("https://automationexercise.com/")

        self.driver.find_element(*self.login_tab_selector).click()
        self.driver.find_element(*self.email_field_selector).send_keys("seleniumremote@gmail.com")
        self.driver.find_element(*self.password_field_selector).send_keys("tester")
        self.driver.find_element(*self.login_button_selector).click()

    def test_multiple_products(self):
        self.driver.find_element(*self.products_tab_selector).click()
        self.driver.set_window_size(400, 800)
        self.driver.maximize_window()

        self.driver.find_element(*self.search_product_field_selector).send_keys("men tshirt")
        self.driver.find_element(*self.add_to_cart_button_selector).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.continue_shopping_button_selector)).click()

        search_field = self.driver.find_element(*self.search_product_field_selector)
        search_field.clear()
        search_field.send_keys("unicorn")
        self.driver.find_element(*self.add_to_cart_button_selector).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.continue_shopping_button_selector)).click()

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
