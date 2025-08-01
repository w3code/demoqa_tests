import allure
from selenium.webdriver.common.by import By


class TextBoxPage:
    def __init__(self, browser):
        self.browser = browser


    @allure.step("Open the text box page")
    def open(self, path):
        self.browser.get(f"https://demoqa.com{path}")
        banner = self.browser.find_element(By.ID, "Ad.Plus-970x250-1")
        self.browser.execute_script("""var elem = arguments[0];elem.parentNode.removeChild(elem);""", banner)


    @allure.step("Fill user name")
    def fill_name(self, name):
        self.browser.find_element(By.ID, "userName").send_keys(name)


    @allure.step("Fill user email address")
    def fill_email(self, email):
        self.browser.find_element(By.ID, "userEmail").send_keys(email)


    @allure.step("Fill user current address")
    def fill_current_address(self, address):
        self.browser.find_element(By.ID, "currentAddress").send_keys(address)


    @allure.step("Fill user permanent address")
    def fill_permanent_address(self, address):
        self.browser.find_element(By.ID, "permanentAddress").send_keys(address)


    @allure.step("Press submit button")
    def press_submit(self):
        submit_button = self.browser.find_element(By.ID, "submit")
        self.browser.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", submit_button)
        submit_button.click()


    @allure.step("Check {field_name} text is correct")
    def get_field_text(self, field_name):
        return self.browser.find_element(By.XPATH, f"//p[@id='{field_name}']").text

