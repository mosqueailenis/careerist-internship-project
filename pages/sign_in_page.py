from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignInPage(Page):
    EMAIL_INPUT = (By.CSS_SELECTOR, "input#email-2")
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[id="field"]')
    LOGIN_BTN = (By.CSS_SELECTOR, "a.login-button.w-button")
    sign_in_page.sign_in_login("mosquea.ilenis@gmail.com", "Florida2015!!!")

    def sign_in_login(self, username, password):
        username_field = self.driver.find_element(*self.EMAIL_INPUT)
        password_field = self.driver.find_element(*self.PASSWORD_INPUT)
        login_button = self.driver.find_element(*self.LOGIN_BTN)

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()



