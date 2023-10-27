from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# @given('Log in to the page')
# def step_when_i_enter_username_and_password(context):
#     username = "mosquea.ilenis@gmail.com"
#     password = "Florida2015!!!"
#     context.app.sign_in_page.sign_in(username, password)
#     context.app.sign_in_page.verify_signin_email()
#     context.app.sign_in_page.verify_signin_password()
#     sleep(1)


@given('Log in to the page mobile web')
def log_in_mobile_web(context):
    username = "mosquea.ilenis@gmail.com"
    password = "Florida2015!!!"
    # context.app.sign_in_page.sign_in(username, password)
    # context.app.sign_in_page.verify_signin_email()
    # context.app.sign_in_page.verify_signin_password()
    context.driver.find_element(By.CSS_SELECTOR, "[type='email']").send_keys(username)
    context.driver.find_element(By.CSS_SELECTOR, "[type='password']").send_keys(password)
    context.driver.find_element(By.CSS_SELECTOR, "[class='login-button w-button']").click()
    sleep(1)
