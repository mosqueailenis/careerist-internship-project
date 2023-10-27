from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Click on settings option')
def step_click_settings(context):
    context.app.settings_page.click_settings_option()
    sleep(1)


@when('Click on settings option mobile web')
def click_settings_mobile_web(context):
    context.app.settings_page.click_settings_mobile_web()
    sleep(1)


@when('Click on Edit profile option')
def step_click_edit_profile(context):
    context.app.settings_page.edit_profile_option()
    sleep(1)


@when('Click on Edit profile option mobile web')
def click_edit_profile_mobile_web(context):
    context.app.settings_page.click_edit_profile_mobile_web()
    sleep(1)


@when('Enter some test information in the input fields')
def step_enter_test_information(context):
    context.app.settings_page.enter_language_field()
    sleep(1)


@when('Enter some test information in the input fields mobile web')
def step_enter_test_information_mobile_web(context):
    context.app.settings_page.enter_language_field()
    sleep(1)


@then('Check the right information is present in the input fields')
def step_verify_entered_information(context):
    context.app.settings_page.get_language_value()
    sleep(1)


@then('Check the right information is present in the input fields mobile web')
def step_verify_entered_information(context):
    context.app.settings_page.get_language_value()
    sleep(1)


@then('Check the "Close" and "Save Changes" buttons clickable')
def check_button_clickable(context):
    context.app.settings_page.check_button_clickable()


@then('Check the "Close" and "Save Changes" buttons clickable mobile web')
def check_button_clickable(context):
    context.app.settings_page.check_button_clickable()



