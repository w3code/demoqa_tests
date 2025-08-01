import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.set_window_size(1920, 1080)
    browser.implicitly_wait(5)

    yield browser

    browser.quit()
