from pages.base_page import Page


class MainPage(Page):
    def open_main(self):
        self.driver.get('https://soft.reelly.io/sign-in')

    def open_main_page_mobile_web(self):
        self.driver.get('https://soft.reelly.io/sign-in')





