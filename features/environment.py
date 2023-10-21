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
        'os': 'Windows',
        'osVersion': '10',
        'browserName': 'Edge',
        'browserVersion': '115.0',
        'sessionName': 'scenario_reelly'
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)
    context.app = Application(context.driver)
    context.driver.set_window_size(1920, 1080)
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()