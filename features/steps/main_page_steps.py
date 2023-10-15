from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open the main page')
def open_main_page(context):
    context.app.main_page.open_main()
    context.driver.refresh()
