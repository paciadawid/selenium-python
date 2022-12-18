from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import BasePage


class ProductsPage(BasePage):
    products_tab_selector = (By.XPATH, "//*[@href='/products']")
    search_product_field_selector = (By.ID, "search_product")
    add_to_cart_button_selector = (By.CLASS_NAME, "add-to-cart")
    continue_shopping_button_selector = (By.CLASS_NAME, "close-modal")

    def add_product_to_cart(self, product_name):
        self.driver.find_element(*self.products_tab_selector).click()
        self.driver.set_window_size(400, 800)
        self.driver.maximize_window()
        search_field = self.driver.find_element(*self.search_product_field_selector)
        search_field.clear()
        search_field.send_keys(product_name)
        self.driver.find_element(*self.add_to_cart_button_selector).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.continue_shopping_button_selector)).click()
