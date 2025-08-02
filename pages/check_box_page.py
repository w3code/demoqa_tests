import allure
from selenium.webdriver.common.by import By


class CheckBoxPage:
    def __init__(self, browser):
        self.browser = browser


    @allure.step("Open the check box page")
    def open(self, path):
        self.browser.get(f"https://demoqa.com{path}")
        banner = self.browser.find_element(By.ID, "Ad.Plus-970x250-1")
        self.browser.execute_script("""var elem = arguments[0];elem.parentNode.removeChild(elem);""", banner)


    @allure.step("Check the Home checkbox")
    def check_home_checkbox(self):
        self.browser.find_element(By.XPATH, "//span[contains(text(),'Home')]").click()


    @allure.step("Click Expand all button")
    def click_expand_all(self):
        self.browser.find_element(By.XPATH, "//button[@title='Expand all']").click()


    def get_checkbox_id_list(self) -> list:
        return [f"tree-node-{check_box_id.text}" for check_box_id in
                             self.browser.find_elements(By.XPATH, "//span[@class='text-success']")]


    def get_checkbox_svg(self, check_box_id):
        return self.browser.find_element(By.XPATH,
                         f"//label[@for='{check_box_id}']//span[@class='rct-checkbox']//*[name()='svg']")
