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
    expected_text = 'Your Amazon Cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty h2").text
    assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'