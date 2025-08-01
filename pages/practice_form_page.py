import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PracticeFormPage:
    def __init__(self, browser):
        self.browser = browser


    @allure.step("Open the practice form page")
    def open(self, path):
        self.browser.get(f"https://demoqa.com{path}")
        banner = self.browser.find_element(By.ID, "Ad.Plus-970x250-1")
        self.browser.execute_script("""var elem = arguments[0];elem.parentNode.removeChild(elem);""", banner)


    @allure.step("Fill user first name")
    def fill_user_first_name(self, user_first_name):
        self.browser.find_element(By.ID, "firstName").send_keys(user_first_name)


    @allure.step("Fill user last name")
    def fill_user_last_name(self, user_last_name):
        self.browser.find_element(By.ID, "lastName").send_keys(user_last_name)


    @allure.step("Fill user email address")
    def fill_user_email(self, user_email):
        self.browser.find_element(By.ID, "userEmail").send_keys(user_email)


    @allure.step("Fill user gender")
    def set_user_gender(self, user_gender):
        self.browser.find_element(By.XPATH, f"//label[text()='{user_gender}']").click()


    @allure.step("Fill user phone number")
    def fill_user_phone_number(self, user_phone_number):
        self.browser.find_element(By.ID, "userNumber").send_keys(user_phone_number)


    @allure.step("Fill user birth date")
    def set_user_birth_date(self, user_birth_day, user_birth_month, user_birth_year):
        self.browser.find_element(By.ID, "dateOfBirthInput").click()
        select_year = self.browser.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']")
        select_year.send_keys(user_birth_year)
        select_month = self.browser.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']")
        select_month.send_keys(user_birth_month)
        self.browser.find_element(By.XPATH, f"//div[contains(@class,'react-datepicker__day--0{user_birth_day}')][contains(@aria-label,'{user_birth_month}')]").click()


    @allure.step("Fill user subject")
    def fill_user_subject(self, user_subject):
        self.browser.find_element(By.ID, "subjectsInput").send_keys(user_subject)
        self.browser.find_element(By.XPATH, f"//div[contains(@class,'subjects-auto-complete__option')]").click()


    @allure.step("Fill user hobby")
    def set_user_hobby(self, user_hobby):
        self.browser.find_element(By.XPATH, f"//label[text()='{user_hobby}']").click()


    @allure.step("Upload user picture")
    def upload_user_picture(self, user_picture):
        self.browser.find_element(By.XPATH, "//input[@id='uploadPicture']").send_keys(user_picture)


    @allure.step("Fill user current address")
    def fill_current_address(self, user_current_address):
        self.browser.find_element(By.ID, "currentAddress").send_keys(user_current_address)


    @allure.step("Fill user state")
    def set_user_state(self, user_state):
        state = self.browser.find_element(By.ID, "state")
        self.browser.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", state)
        state.click()
        self.browser.find_element(By.XPATH, f"//div[contains(text(),'{user_state}')]").click()


    @allure.step("Fill user city")
    def set_user_city(self, user_city):
        self.browser.find_element(By.ID, "city").click()
        self.browser.find_element(By.XPATH, f"//div[contains(text(),'{user_city}')]").click()


    @allure.step("Press submit button")
    def press_submit(self):
        self.browser.find_element(By.ID, "submit").click()


    @allure.step("Check title text")
    def get_title_text(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))).text


    @allure.step("Check {field_name}")
    def get_field_text(self, field_name):
        return self.browser.find_element(By.XPATH, f"//td[preceding-sibling::td[contains(.,'{field_name}')]]").text


    @allure.step("Close modal window")
    def close_modal(self):
        self.browser.find_element(By.XPATH, f"//button[@id='closeLargeModal']").click()
