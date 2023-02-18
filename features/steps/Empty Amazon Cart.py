from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.ID, 'nav-cart').click()

@then('Verify that Cart is empty')
def verify_click_result(context):