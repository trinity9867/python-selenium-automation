from pages.base_page import Page


class MainPage(Page):

    def open_main(self):
        self.click(*self.SEARCH_ICON)