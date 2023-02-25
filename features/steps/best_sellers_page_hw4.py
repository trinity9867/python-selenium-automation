from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Best Sellers')
def click_best_sellers(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-content-id=nav_cs_bestsellers]").click()


@then('Verify that {expected_count} links are shown')
def verify_click_result_text(context, expected_count):
    all_links = context.driver.find_elements(By.XPATH, "//div[@class='_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq']/ul/li/div/a")
    actual_count = len(all_links)
    assert expected_count== str(actual_count) , f'Expected {expected_count} but got actual {actual_count}'
    print('Test Passed')


