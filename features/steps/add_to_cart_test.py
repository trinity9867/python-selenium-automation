from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then


AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a/span[@class='a-price']")
ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
CART = (By.ID, 'nav-cart-count')













@then('Verify that cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(*CART).text
    assert expected_count == actual_text, f'Expected {expected_count}, but actual {actual_text}'