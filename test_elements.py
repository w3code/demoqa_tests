import random

import allure

from data import TestData
from pages.check_box_page import CheckBoxPage
from pages.radio_button_page import RadioButtonPage
from pages.text_box_page import TextBoxPage


@allure.tag("WEB")
@allure.title("Test Text Box")
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


@allure.tag("WEB")
@allure.title("Test Check Box")
@allure.label("owner", "w3code")
@allure.feature("Check checkboxes")
def test_check_box(browser):
    page = CheckBoxPage(browser)

    def verify_is_checkboxes_checked(checkbox_id_list: list):
        for checkbox_id in checkbox_id_list:
            svg_el = page.get_checkbox_svg(checkbox_id)
            assert "rct-icon-check" in svg_el.get_attribute("class"), f"Verify {checkbox_id} id error"


    page.open("/checkbox")
    page.check_home_checkbox()
    page.click_expand_all()

    verify_is_checkboxes_checked(page.get_checkbox_id_list())


@allure.tag("WEB")
@allure.title("Test Radio Button")
@allure.label("owner", "w3code")
@allure.feature("Test radio buttons")
def test_radio_button(browser):

    def verify_success_text(testing_radio):
        assert page.get_success_text() == testing_radio

    testing_radio = random.choice(["Impressive", "Yes"])

    page = RadioButtonPage(browser)

    page.open("/radio-button")
    page.check_random_radiobox(testing_radio)

    verify_success_text(testing_radio)
