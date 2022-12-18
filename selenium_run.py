# selenium 4
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get("https://automationexercise.com/")


driver.find_element(By.ID, "subscribe")

driver.find_element(By.CLASS_NAME, "logo")
driver.find_element(By.CLASS_NAME, "fa-shopping-cart")
driver.find_element(By.ID, "susbscribe_email")
driver.find_element(By.CLASS_NAME, "fa-angle-right")
driver.find_element(By.CLASS_NAME, "brands_products")
driver.find_element(By.ID, "footer")

# css selectors
driver.find_element(By.CSS_SELECTOR, ".logo img")
driver.find_element(By.CSS_SELECTOR, ".navbar-nav a[href='/view_cart']")
driver.find_element(By.CSS_SELECTOR, "#susbscribe_email")
driver.find_element(By.CSS_SELECTOR, "[href='#slider-carousel'] .fa-angle-right")
driver.find_element(By.CSS_SELECTOR, ".brands_products > h2")
driver.find_element(By.CSS_SELECTOR, "#footer")

# xpath
driver.find_element(By.XPATH, "//*[contains(@class,'logo')]//img")
driver.find_element(By.XPATH, "//a[@href='/view_cart']")
driver.find_element(By.XPATH, "//*[@id='susbscribe_email']")
driver.find_element(By.XPATH, "//*[@href='#slider-carousel' and contains(@class, 'right')]/i")
driver.find_element(By.XPATH, "//*[@class='brands_products']/h2")
driver.find_element(By.XPATH, "//*[@id='footer']")


driver.quit()
