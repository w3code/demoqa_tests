import allure
from selenium.webdriver.common.by import By


class RadioButtonPage:
    def __init__(self, browser):
        self.browser = browser


    @allure.step("Open the check box page")
    def open(self, path):
        self.browser.get(f"https://demoqa.com{path}")
        banner = self.browser.find_element(By.ID, "Ad.Plus-970x250-1")
        self.browser.execute_script("""var elem = arguments[0];elem.parentNode.removeChild(elem);""", banner)


    @allure.step("Check the Home checkbox")
    def check_random_radiobox(self, radio):
        self.browser.find_element(By.XPATH, f"//label[contains(text(),'{radio}')]").click()


    def get_success_text(self):
            return self.browser.find_element(By.XPATH, "//span[@class='text-success']").text