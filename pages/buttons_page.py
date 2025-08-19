import allure
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains


class ButtonsPage:
    def __init__(self, browser):
        self.browser = browser


    @allure.step("Open the Web Tables page")
    def open(self, path):
        self.browser.get(f"https://demoqa.com{path}")
        banner = self.browser.find_element(By.ID, "Ad.Plus-970x250-1")
        self.browser.execute_script("""var elem = arguments[0];elem.parentNode.removeChild(elem);""", banner)


    @allure.step("Button double click")
    def double_click(self):
        double_click_me_btn = self.browser.find_element(By.ID, "doubleClickBtn")
        ActionChains(self.browser).double_click(double_click_me_btn).perform()


    def get_double_click_message(self):
        return self.browser.find_element(By.ID, "doubleClickMessage").text


    @allure.step("Button right click")
    def right_click(self):
        right_click_me_btn = self.browser.find_element(By.ID, "rightClickBtn")
        ActionChains(self.browser).context_click(right_click_me_btn).perform()


    def get_right_click_message(self):
        return self.browser.find_element(By.ID, "rightClickMessage").text


    @allure.step("Click button with dynamic ID")
    def click_button_with_dynamic_id(self):
        self.browser.find_element(By.XPATH, "//button[.='Click Me']").click()


    def get_dynamic_click_message(self):
        return self.browser.find_element(By.ID, "dynamicClickMessage").text