from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given ('Log in to the page')
def log_in_page(context):
    username = "mosquea.ilenis@gmail.com"
    password = "Florida2015!!!"



    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()