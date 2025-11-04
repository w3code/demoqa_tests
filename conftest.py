import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.bidi.browser import Browser
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    # browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    options = Options()
    selenoid_capabilities = {
    "browserName": "chrome",
    "browserVersion": "128.0",
    "selenoid:options": {
        "enableVideo": False
    }
}
    options.capabilities.update(selenoid_capabilities)
    browser = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=options
    )
    browser.set_window_size(1920, 1080)
    browser.implicitly_wait(5)

    yield browser

    browser.quit()
