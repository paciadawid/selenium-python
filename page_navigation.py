from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get("https://automationexercise.com/")

driver.find_element(By.XPATH, "//*[@href='/products']").click()

# try:
#     WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, "dismiss-button"))).click()
# except NoSuchElementException:
#     pass
driver.set_window_size(400, 800)
driver.maximize_window()

driver.find_element(By.ID, "search_product").send_keys("unicorn")
driver.find_element(By.ID, "submit_search").click()

products = driver.find_elements(By.CLASS_NAME, "single-products")
assert len(products) >= 2

driver.quit()

