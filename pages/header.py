from selenium.webdriver.common.by import By
from pages.base_page import  Page

from pages.base_page import Page

class Header(Page):
    pass
AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')


    def input_search_text(self):
        self.input_text('coffe', *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)