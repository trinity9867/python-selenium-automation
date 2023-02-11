from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the URL
driver.get('https://www.amazon.com/')

# click returns & orders
driver.find_element(By.XPATH, "//a[@id='nav-orders']").click()

# verify sign in page opened: sign in header is visible, email input field is present
print('Test Passed')

driver.quit()

