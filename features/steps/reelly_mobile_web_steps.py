from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

EMAIL_INPUT = (By.CSS_SELECTOR, "input#username")
PASSWORD_INPUT = (By.CSS_SELECTOR, 'input#password')
LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
COMPANY_INPUT = (By.CSS_SELECTOR, '[class="field-form-block w-input"][wized="companyInputProfile"]')
LANGUAGE_INPUT = (By.CSS_SELECTOR, 'input#Languages')
CLOSE_BUTTON = (By.CSS_SELECTOR, 'a[href="/settings"].close-button')
SAVE_CHANGES_BUTTON = (By.CSS_SELECTOR, 'div[w-el-onclick-0-0="8916f00b-660d-4595-97bc-e7e445cb0988-0-0"]')
LANGUAGE_Input = 'English'
SETTINGS_LINK = (By.CSS_SELECTOR, 'a.menu-button-block.w-inline-block[href="/settings"]')
EDIT_PROFILE_BTN = (By.CSS_SELECTOR, 'a[href="/profile-edit"].page-setting-block')


@given('Open the main page mobile web')
def open_main_page_mobile_web(context):
    context.driver.get("https://soft.reelly.io/sign-in")
    sleep(1)


@given('Log in to the page mobile web')
def log_in_mobile_web(context):
    email_input = context.driver.find_element(*EMAIL_INPUT)
    password_input = context.driver.find_element(*PASSWORD_INPUT)
    login_btn = context.driver.find_element(*LOGIN_BTN)

    email_input.send_keys("mosquea.ilenis@gmail.com")
    password_input.send_keys("Florida2015!!!")
    login_btn.click()


@when('Click on settings option mobile web')
def click_settings_mobile_web(context):
    settings_link = context.driver.find_element(*SETTINGS_LINK)
    settings_link.click()
    sleep(1)


@when('Click on Edit profile option mobile web')
def click_edit_profile_mobile_web(context):
    edit_profile_button = context.driver.find_element(*EDIT_PROFILE_BTN)
    edit_profile_button.click()
    sleep(1)


@when('Enter some test information in the input fields mobile web')
def enter_test_information_mobile_web(context):
    company_input = context.driver.find_element(*COMPANY_INPUT)
    language_input = context.driver.find_element(*LANGUAGE_INPUT)

    company_input.clear()
    company_input.send_keys("Test Company")

    language_input.clear()
    language_input.send_keys("English")
    sleep(1)


@then('Check the right information is present in the input fields mobile web')
def check_information_mobile_web(context):
    company_input = context.driver.find_element(*COMPANY_INPUT)
    language_input = context.driver.find_element(*LANGUAGE_INPUT)

    assert company_input.get_attribute("value") == "Test Company"
    assert language_input.get_attribute("value") == "English"
    sleep(1)


@then('Check the "Close" and "Save Changes" buttons clickable mobile web')
def check_buttons_clickable_mobile_web(context):
    close_button = context.driver.find_element(*CLOSE_BUTTON)
    save_changes_button = context.driver.find_element(*SAVE_CHANGES_BUTTON)

    assert close_button.is_enabled()
    assert save_changes_button.is_enabled()
    sleep(1)



