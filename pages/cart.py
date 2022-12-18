from selenium.webdriver.common.by import By

from pages.base import BasePage


class CartPage(BasePage):
    cart_tab_selector = (By.XPATH, "//*[@href='/view_cart']")
    checkout_button_selector = (By.CLASS_NAME, "check_out")
    close_modal_button_selector = (By.CLASS_NAME, "close-checkout-modal")

    def view_cart(self):
        self.driver.find_element(*self.cart_tab_selector).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button_selector).click()

    def check_if_popup_appeared(self):
        self.driver.find_element(*self.close_modal_button_selector).click()
