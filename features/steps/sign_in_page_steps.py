from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Log in to the page')
def step_when_i_enter_username_and_password(context):
    username = "mosquea.ilenis@gmail.com"
    password = "Florida2015!!!"
    context.app.sign_in_page.sign_in(username, password)
    context.app.sign_in_page.verify_signin_opened()

