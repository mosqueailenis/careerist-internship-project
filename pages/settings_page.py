from time import sleep

from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SettingsPage(Page):

    LANGUAGE_Input = 'English'
    SETTINGS_LINK = (By.CSS_SELECTOR, 'a.menu-button-block.w-inline-block[href="/settings"]')
    EDIT_PROFILE_BTN = (By.CSS_SELECTOR, 'a[href="/profile-edit"].page-setting-block')
    LANGUAGE_INPUT = (By.CSS_SELECTOR, 'input#Languages')
    MENU_BTN = (By.CSS_SELECTOR, '#w-node-b3e2d1dd-1dc5-4f3f-14dd-85ad6c4b0445-bfd82bd6 > div.search_block1 > a.menu-button-wrapper.w-inline-block')
    CLOSE_BUTTON = (By.CSS_SELECTOR, 'a[href="/settings"].close-button')
    SAVE_CHANGES_BUTTON = (By.CSS_SELECTOR, 'div[w-el-onclick-0-0="8916f00b-660d-4595-97bc-e7e445cb0988-0-0"]')

    def click_settings_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SETTINGS_LINK)
        )
        settings_option = self.driver.find_element(*self.SETTINGS_LINK)
        settings_option.click()

    def click_settings_mobile_web(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.MENU_BTN)
        )
        settings_option = self.driver.find_element(*self.MENU_BTN)
        settings_option.click()

    def edit_profile_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.EDIT_PROFILE_BTN)
        )
        edit_profile_option = self.find_element(*self.EDIT_PROFILE_BTN)
        edit_profile_option.click()

    def click_edit_profile_mobile_web(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.EDIT_PROFILE_BTN)
        )
        edit_profile_option = self.find_element(*self.EDIT_PROFILE_BTN)
        edit_profile_option.click()

    def enter_language_field(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.LANGUAGE_INPUT)
        )
        language_input = self.driver.find_element(*self.LANGUAGE_INPUT)
        language_input.clear()
        self.input_text('English', *self.LANGUAGE_INPUT)
        print(f'Language field value: {language_input.get_attribute("value")}')

    def get_language_value(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.LANGUAGE_INPUT)
        )
        language_input = self.driver.find_element(*self.LANGUAGE_INPUT)
        return language_input.get_attribute("value")

    def check_button_clickable(self):
        close_button = self.find_element(*self.CLOSE_BUTTON)
        save_changes_button = self.find_element(*self.SAVE_CHANGES_BUTTON)
        return close_button.is_enabled(), save_changes_button.is_enabled()


