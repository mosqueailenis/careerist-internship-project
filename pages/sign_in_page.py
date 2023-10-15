from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignInPage(Page):
    EMAIL_INPUT = (By.CSS_SELECTOR, "input#email-2")
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[id="field"]')
    LOGIN_BTN = (By.CSS_SELECTOR, "a.login-button.w-button")

    def step_when_i_enter_username_and_password(self, username, password):
        username_field = self.driver.find_element(*self.EMAIL_INPUT)
        password_field = self.driver.find_element(*self.PASSWORD_INPUT)
        login_button = self.driver.find_element(*self.LOGIN_BTN)

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

    def enter_username(self, username):
        username_field = self.driver.find_element(*self.EMAIL_INPUT)
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(*self.PASSWORD_INPUT)
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(*self.LOGIN_BTN)
        login_button.click()

    def sign_in(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def verify_signin_opened(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.name_text_account'))
        )

