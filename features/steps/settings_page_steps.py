from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Click on settings option')
def step_click_settings(context):
    context.app.settings_page.click_settings_option()


@when('Click on Edit profile option')
def step_click_edit_profile(context):
    context.app.settings_page.edit_profile_option()


@when('Enter some test information in the input fields')
def step_enter_test_information(context):
    context.app.settings_page.step_enter_test_information()
