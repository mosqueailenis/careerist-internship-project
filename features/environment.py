from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from app.application import Application
from support.logger import logger


def browser_init(context):
    """
    :param context: Behave context
    """

    # service = Service(executable_path='/Users/ilenismosquea/QA/python-selenium-automation/chromedriver')
    # context.driver = webdriver.Chrome(service=service)
    #
    # context.driver.maximize_window()
    #
    # context.driver.implicitly_wait(4)
    # context.driver.wait = WebDriverWait(context.driver, 10)
    #
    # context.app = Application(context.driver)

    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    # context.driver.wait = WebDriverWait(context.driver, 10)
    #
    # context.app = Application(context.driver)

    ## HEADLESS MODE ####

    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # service = Service(executable_path='/Users/ilenismosquea/Downloads/careerist-internship-project/chromedriver')
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    # Firefox #

    # service = Service(executable_path='/Users/ilenismosquea/Downloads/careerist-internship-project/geckodriver')
    # context.driver = webdriver.Firefox(service=service)
    #
    # context.driver.set_window_size(1920,1080)
    # context.driver.implicitly_wait(4)
    # context.driver.wait = WebDriverWait(context.driver, 10)
    # context.app = Application(context.driver)




 ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'ilenismosquea_gEX0wS'
    bs_key = 'q6BsM4L9LqgPAv5GYpW2'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        "osVersion": "8.1",
        "deviceName": "Samsung Galaxy Note 9",
        "local": "false",
        "debug": "true",
        'browserName': 'Chrome',
        'sessionName': 'scenario_name'
        # 'os': 'Windows',
        # 'osVersion': '10',
        # 'browserName': 'Edge',
        # 'browserVersion': '115.0',
        # 'sessionName': 'scenario_reelly'
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)
    context.app = Application(context.driver)
    context.driver.set_window_size(1920, 1080)
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)



    #### Mobile emulation ####

#     mobile_emulation = {
#
#        "deviceName": "Pixel 5", }
#
#     chrome_options = webdriver.ChromeOptions()
#
#     chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
#
#     context.driver = webdriver.Chrome(
#
#      options=chrome_options
#
#     )
# ##
#
#     context.driver.maximize_window()
#     context.driver.implicitly_wait(4)
#     context.driver.wait = WebDriverWait(context.driver, 10)
#     context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    # logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')
