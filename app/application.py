from pages.main_page import MainPage
from pages.sign_in_page import SignInPage


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.sign_in_page = SignInPage(driver)