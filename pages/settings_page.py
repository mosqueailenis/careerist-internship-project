from pages.base_page import Page
from selenium.webdriver.common.by import By


class SettingsPage(Page):
    SETTINGS_LINK = (By.CSS_SELECTOR, 'a.menu-button-block.w-inline-block[href="/settings"]')
    EDIT_PROFILE_BTN =(By.CSS_SELECTOR, 'a[href="/profile-edit"].page-setting-block')
    COMPANY_INPUT = (By.CSS_SELECTOR, '[class="field-form-block w-input"][wized="companyInputProfile"]')
    LANGUAGE_INPUT = (By.CSS_SELECTOR, 'input#Languages')

    def click_settings_option(self):
        settings_option = self.driver.find_element(*self.SETTINGS_LINK)
        settings_option.click()

    def edit_profile_option(self):
        edit_profile_option = self.find_element(*self.EDIT_PROFILE_BTN)
        edit_profile_option.click()

    def step_enter_test_information(self, company_name, language_input):
        company_name = self.find_element(*self.COMPANY_INPUT)
        language_input = self.find_element(*self.LANGUAGE_INPUT)

        company_name.clear()
        company_name.send_keys(company_name)

        language_input.clear()
        language_input.send_keys(language_input)




