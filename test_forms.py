import allure

from data import TestData
from pages.practice_form_page import PracticeFormPage

@allure.tag("WEB")
@allure.title("Test Practice Form")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "w3code")
@allure.feature("Fill registration form")
def test_practice_form(browser):
    page = PracticeFormPage(browser)
    test_data = TestData()

    def check_is_title_correct():
        assert page.get_title_text() == "Thanks for submitting the form", "Title is incorrect"


    def check_is_data_correct(field, data):
        assert page.get_field_text(field) == data, f"Field '{field}' is incorrect"


    page.open("/automation-practice-form")
    page.fill_user_first_name(test_data.user_first_name)
    page.fill_user_last_name(test_data.user_last_name)
    page.fill_user_email(test_data.user_email)
    page.set_user_gender(test_data.user_gender)
    page.fill_user_phone_number(test_data.user_phone_number)
    page.set_user_birth_date(test_data.user_birth_day, test_data.user_birth_month, test_data.user_birth_year)
    page.fill_user_subject(test_data.user_subject)
    page.set_user_hobby(test_data.user_hobby)
    page.upload_user_picture(test_data.user_picture)
    page.fill_current_address(test_data.user_current_address)
    page.set_user_state(test_data.user_state)
    page.set_user_city(test_data.user_city)
    page.press_submit()

    check_is_title_correct()
    check_is_data_correct("Student Name", test_data.user_first_name + " " + test_data.user_last_name)
    check_is_data_correct("Student Email", test_data.user_email)
    check_is_data_correct("Gender", test_data.user_gender)
    check_is_data_correct("Mobile", test_data.user_phone_number)
    check_is_data_correct("Date of Birth", test_data.user_birth_day + " " + test_data.user_birth_month + "," + test_data.user_birth_year)
    check_is_data_correct("Subjects", test_data.user_subject)
    check_is_data_correct("Hobbies", test_data.user_hobby)
    check_is_data_correct("Picture", "picture.jpg")
    check_is_data_correct("Address", test_data.user_current_address)
    check_is_data_correct("State and City", test_data.user_state + " " + test_data.user_city)

    page.close_modal()
