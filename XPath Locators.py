


# By Xpath, tag and attribute
Amazon logo = driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
Amazon logo = driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
Need help link = driver.find.element(By.XPATH, "//span[@class='a-expander-prompt']")


# By ID
Continue button= driver.find_element(By.ID, "//input[@id='continue']")
Other issues with Sign-in link = driver.find_element(By.ID, "//a[@id='ap-other-signin-issues-link']")
Create your Amazon account button = driver.find_element(By.ID, "//a[@id='createAccountSubmit']")
Forgot your password link = driver.find.element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")

# By xpath, multiple attributes
Conditions of Use link = driver.find_element(By.XPATH, "//a[@class='a-link-normal' and @href='/gp/help/customer/display.html/ref=ap_desktop_footer_cou?ie=UTF8&nodeId=508088']")
Privacy Notice link = driver.find_element(By.XPATH, "//a[@class='a-link-normal' and @href='/gp/help/customer/display.html/ref=ap_desktop_footer_privacy_notice?ie=UTF8&nodeId=468496']")