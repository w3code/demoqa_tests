import allure
from selenium.webdriver.common.by import By


class WebTablesPage:
    def __init__(self, browser):
        self.browser = browser


    @allure.step("Open the Web Tables page")
    def open(self, path):
        self.browser.get(f"https://demoqa.com{path}")
        banner = self.browser.find_element(By.ID, "Ad.Plus-970x250-1")
        self.browser.execute_script("""var elem = arguments[0];elem.parentNode.removeChild(elem);""", banner)


    @allure.step("Fill form")
    def fill_form(self, first_name, last_name, email, age, salary, department):
        el_first_name = self.browser.find_element(By.XPATH, "//input[@id='firstName']")
        el_first_name.clear()
        el_first_name.send_keys(first_name)

        el_last_name = self.browser.find_element(By.XPATH, "//input[@id='lastName']")
        el_last_name.clear()
        el_last_name.send_keys(last_name)

        el_user_email = self.browser.find_element(By.XPATH, "//input[@id='userEmail']")
        el_user_email.clear()
        el_user_email.send_keys(email)

        el_age = self.browser.find_element(By.XPATH, "//input[@id='age']")
        el_age.clear()
        el_age.send_keys(age)

        el_salary = self.browser.find_element(By.XPATH, "//input[@id='salary']")
        el_salary.clear()
        el_salary.send_keys(salary)

        el_department = self.browser.find_element(By.XPATH, "//input[@id='department']")
        el_department.clear()
        el_department.send_keys(department)

        self.browser.find_element(By.XPATH, "//button[@id='submit']").click()


    @allure.step("Add row")
    def add_row(self):
        self.browser.find_element(By.XPATH, "//button[@id='addNewRecordButton']").click()


    @allure.step("Edit first row")
    def edit_first_row(self):
        self.browser.find_element(By.XPATH, "//span[contains(@id, 'edit-record')]").click()


    @allure.step("Delete first row")
    def delete_first_row(self):
        self.browser.find_element(By.XPATH, "//span[contains(@id, 'delete-record')]").click()


    @allure.step("Get No Data text")
    def get_no_data_text(self):
        return self.browser.find_element(By.XPATH, "//div[@class='rt-noData']").text


    def parse_first_row(self):
        first_row_elements = self.browser.find_element(By.XPATH, "//div[@class='rt-tr -odd']")
        return first_row_elements.text.split('\n')



