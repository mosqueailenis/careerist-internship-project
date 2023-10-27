from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from support.logger import logger


class Page:
    EMAIL_INPUT = (By.ID, '#email-2')
    PASSWORD_INPUT = (By.ID, '#field')
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    COMPANY_INPUT = (By.CSS_SELECTOR, '[class="field-form-block w-input"][wized="companyInputProfile"]')
    LANGUAGE_INPUT = (By.CSS_SELECTOR, 'input#Languages')
    CLOSE_BUTTON = (By.CSS_SELECTOR, 'a[href="/settings"].close-button')
    SAVE_CHANGES_BUTTON = (By.CSS_SELECTOR, 'div[w-el-onclick-0-0="8916f00b-660d-4595-97bc-e7e445cb0988-0-0"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

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

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.send_keys(text)

    def get_current_window(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print(all_windows)
        print(f'Switching to {all_windows[1]}')
        self.driver.switch_to.window(all_windows[1])

    def get_windows(self):
        windows = self.driver.window_handles
        print(windows)
        return windows

    def switch_to_window(self, window_id):
        print(f'Switching to {window_id}')
        self.driver.switch_to.window(window_id)

    def close_page(self):
        self.driver.close()

    def wait_for_element_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable: {locator}'
        )

    def wait_for_element_clickable_click(self, *locator):
        e = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable: {locator}'
        )
        e.click()

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, \
            f'Error, expected {expected_text} did not match actual {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, \
            f'Error, expected partial text {expected_text} not in {actual_text}'

    def wait_for_element_appear(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element did not appear: {locator}')

    def wait_for_element_disappear(self, *locator):
        self.wait.until(
                EC.invisibility_of_element_located(locator),
                message=f'Element did not disappear: {locator}'
            )

    def verify_partial_url(self, expected_part_of_url):
        self.wait.until(EC.url_contains(expected_part_of_url))

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)