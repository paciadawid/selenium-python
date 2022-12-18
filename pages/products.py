from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import BasePage


class ProductsPage(BasePage):
    products_tab_selector = (By.XPATH, "//*[@href='/products']")
    search_product_field_selector = (By.ID, "search_product")
    add_to_cart_button_selector = (By.CSS_SELECTOR, ".overlay-content .add-to-cart")
    continue_shopping_button_selector = (By.CLASS_NAME, "close-modal")
    product_info_selector = (By.CLASS_NAME, "productinfo")

    def add_products_to_cart(self, product_name, number_of_items):
        for i in range(number_of_items):
            self.add_product_to_cart(product_name)

    def add_product_to_cart(self, product_name):
        self.driver.find_element(*self.products_tab_selector).click()
        try:
            search_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.search_product_field_selector))
        except (NoSuchElementException, TimeoutException):
            self.driver.set_window_size(400, 800)
            self.driver.maximize_window()
            search_field = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.search_product_field_selector)).click()

        search_field.clear()
        search_field.send_keys(product_name)

        productinfo = self.driver.find_element(*self.product_info_selector)
        actions = ActionChains(self.driver)
        actions.move_to_element(productinfo)
        actions.perform()

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.add_to_cart_button_selector)).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.continue_shopping_button_selector)).click()
