import random

import allure

from data import TestData
from pages.check_box_page import CheckBoxPage
from pages.radio_button_page import RadioButtonPage
from pages.text_box_page import TextBoxPage
from pages.web_tables_page import WebTablesPage


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


@allure.tag("WEB")
@allure.title("Test Web Tables Delete Items")
@allure.label("owner", "w3code")
@allure.feature("Test Web Tables Delete Items")
def test_web_tables_delete_items(browser):

    page = WebTablesPage(browser)

    page.open("/webtables")
    page.delete_first_row()
    page.delete_first_row()
    page.delete_first_row()

    assert page.get_no_data_text() == "No rows found", "No data element found"


@allure.tag("WEB")
@allure.title("Test Web Tables edit Items")
@allure.label("owner", "w3code")
@allure.feature("Test Web Tables edit Items")
def test_web_tables_edit_item(browser):

    page = WebTablesPage(browser)
    test_data = TestData()

    page.open("/webtables")
    page.edit_first_row()
    page.fill_form(test_data.user_first_name,
                   test_data.user_last_name,
                   test_data.user_email,
                   test_data.user_age,
                   test_data.user_salary,
                   test_data.user_department)

    edited_data = page.parse_first_row()

    assert test_data.user_first_name == edited_data[0],  "First name incorrect"
    assert test_data.user_last_name == edited_data[1], "Last name incorrect"
    assert test_data.user_age == edited_data[2], "Age incorrect"
    assert test_data.user_email == edited_data[3], "Email incorrect"
    assert test_data.user_salary == edited_data[4], "Salary incorrect"
    assert test_data.user_department == edited_data[5], "Department incorrect"


@allure.tag("WEB")
@allure.title("Test Web Tables add Items")
@allure.label("owner", "w3code")
@allure.feature("Test Web Tables add Items")
def test_web_tables_add_item(browser):

    page = WebTablesPage(browser)
    test_data = TestData()

    page.open("/webtables")
    page.delete_first_row()
    page.delete_first_row()
    page.delete_first_row()
    page.add_row()
    page.fill_form(test_data.user_first_name,
                   test_data.user_last_name,
                   test_data.user_email,
                   test_data.user_age,
                   test_data.user_salary,
                   test_data.user_department)

    added_data = page.parse_first_row()

    assert test_data.user_first_name == added_data[0],  "First name incorrect"
    assert test_data.user_last_name == added_data[1], "Last name incorrect"
    assert test_data.user_age == added_data[2], "Age incorrect"
    assert test_data.user_email == added_data[3], "Email incorrect"
    assert test_data.user_salary == added_data[4], "Salary incorrect"
    assert test_data.user_department == added_data[5], "Department incorrect"
