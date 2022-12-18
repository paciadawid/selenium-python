from selenium.webdriver.common.by import By

from pages.base import BasePage


class CheckoutPage(BasePage):
    cart_price_selector = (By.CLASS_NAME, "cart_total_price")

    def get_product_prices(self):
        prices_elements = self.driver.find_elements(*self.cart_price_selector)
        product_prices = []
        for price_element in prices_elements[:-1]:
            product_prices.append(int(price_element.text[3:]))
        return product_prices

    def get_total_amount(self):
        prices_elements = self.driver.find_elements(*self.cart_price_selector)
        total_amount = int(prices_elements[-1].text[3:])
        return total_amount
