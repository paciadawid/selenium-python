from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get("https://www.ryanair.com/")

driver.find_element(By.CLASS_NAME, "cookie-popup-with-overlay__button").click()
driver.find_element(By.CSS_SELECTOR, "[data-ref='flight-search-trip-type__one-way-trip']").click()

driver.find_element(By.ID, "input-button__departure").click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-id='SZY']"))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-id='STN']"))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-id='2022-12-22']"))).click()

driver.find_element(By.CSS_SELECTOR, "[data-ref='terms-of-use__terms-checkbox']").click()
driver.find_element(By.CSS_SELECTOR, "[data-ref='flight-search-widget__cta']").click()


WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//flight-price"))).click()


driver.quit()