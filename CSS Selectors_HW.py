from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')

# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')

Amazon logo = "i[aria-label=Amazon]"

Create account = "h1[class=a-spacing-small]")

Your name = "#ap_customer_name"

Email = "#ap_email"


Password = "#ap_password"


Re-enter password = "#ap_password_check"


Continue = "#continue"

Conditions of Use = "//a[contains(@href,'ap_register_notification_condition_of_use?')]")

Privacy Notice = "//a[contains(@href,'ap_register_notification_privacy_notice?')]")

Sign In = "//a[contains(@href,'ap/signin?')]")



