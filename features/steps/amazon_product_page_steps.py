from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from behave import when, given, then
from time import sleep


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
PRODUCT_PRICE = (By.ID, 'corePrice_feature_div')

COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")

THUMBNAIL_IMG = (By.CSS_SELECTOR, '#altImages input.a-button-input')




@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    #sleep(4)


@when('Store product name and price')
def get_product_name(context):
    context.product_name = context.driver.wait.until(EC.visibility_of_element_located(PRODUCT_NAME)).text
    #context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')
    context.product_price = context.driver.find_element(*PRODUCT_PRICE).text
    print(f'Current product price: {context.product_price}')



    # Example with THUMBNAIL_IMG:
    # all_imgs = context.driver.find_elements(*THUMBNAIL_IMG)
    #
    # for img in all_imgs:
    #     img.click()