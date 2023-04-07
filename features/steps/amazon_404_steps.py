from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


PRIVACY_LINK = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")



@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')



@given('Store original window')
def store_current_window(context):
    context.current_window = context.driver.current_window_handle
    print(context.current_window)


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice(context):
    context.driver.find_element(*PRIVACY_LINK).click()


@when('Switch to the newly opened window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.current_window_handles # [CDwindow-BF1E6FD5D85C3E3410C789AC2E885646, CDwindow-BF1E6FD5D85C3E3410C789AC2E885646]
    context.driver.switch_to.window(windows[1])


    context.current_window = context.driver.current_window_handle
    print('AFTER WE SWITCHED:')
    print(context.current_window)



