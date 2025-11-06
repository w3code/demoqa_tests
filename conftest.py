import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.bidi.browser import Browser
from webdriver_manager.chrome import ChromeDriverManager

from utils import attach


DEFAULT_BROWSER_VERSION = "128.0"

def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='128.0'
    )

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture
def browser(request):
    # browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION

    options = Options()
    selenoid_capabilities = {
    "browserName": "chrome",
    "browserVersion": browser_version,
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": True,
        "pageLoadStrategy": "eager"
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    browser = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.set_window_size(1920, 1080)
    browser.implicitly_wait(5)

    yield browser

    attach.add_screenshot(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
