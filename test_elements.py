import allure

from data import TestData
from pages.text_box_page import TextBoxPage


@allure.tag("WEB")
@allure.title("Test Text Box")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "w3code")
@allure.feature("Fill text box form")
def test_text_box(browser):
    page = TextBoxPage(browser)
    test_data = TestData()

    def check_is_data_correct(field_id, data):
        assert data in page.get_field_text(field_id)


    page.open("/text-box")
    page.fill_name(f"{test_data.user_first_name} {test_data.user_last_name}")
    page.fill_email(test_data.user_email)
    page.fill_current_address(test_data.user_current_address)
    page.fill_permanent_address(test_data.user_current_address)
    page.press_submit()

    check_is_data_correct("name", f"{test_data.user_first_name} {test_data.user_last_name}")
    check_is_data_correct("email", test_data.user_email)
    check_is_data_correct("currentAddress", test_data.user_current_address)
    check_is_data_correct("permanentAddress", test_data.user_current_address)
