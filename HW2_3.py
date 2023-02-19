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
expected_text = 'Sign in'
actual_text = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'

print('Test Passed')

driver.quit()

