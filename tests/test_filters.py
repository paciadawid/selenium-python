import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class TestFilters(unittest.TestCase):

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("https://automationexercise.com/")
        print(self.driver.get_window_size())

        self.driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']").send_keys("seleniumremote@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']").send_keys("tester")
        self.driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']").click()

    def test_category(self):
        self.driver.find_element(By.CSS_SELECTOR, ".panel-title > a").click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".panel-body li")))
        self.driver.find_element(By.CLASS_NAME, "single-products")

    def test_brands(self):
        brand = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".brands-name a")))
        number_of_items = brand.find_element(By.CSS_SELECTOR, "span").text
        number_of_items = int(number_of_items[1:-1])
        brand.click()
        products = self.driver.find_elements(By.CLASS_NAME, "single-products")
        self.assertEqual(number_of_items, len(products))

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
