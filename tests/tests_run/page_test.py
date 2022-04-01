import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, checkboxes_page,hovers_page, users_page, inputs_page, dropdown_page, add_remove_page
from tests.page_objects import date_picker, basic_auth, form, key_presses, drag_and_drop, status_code, IFrame
from time import sleep


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/emil.archacki/PycharmProjects/seleniumWebdriverGit/chromedriver.exe')
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    def test2_checkboxes(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_visible(self.driver))

    def test3_hovers(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hover_content_displayed(self.driver))
        hovers_page.hover_over_element_and_click(self.driver)
        self.assertTrue(users_page.error_info_displayed(self.driver))

    def test4_inputs_visibility(self):
        inputs_page.click_inputs_tabs(self.driver)
        self.assertTrue(inputs_page.input_content_visible(self.driver))

    def test5_inputs_correct_input(self):
        inputs_page.click_inputs_tabs(self.driver)
        self.assertTrue(inputs_page.send_correct_keys_to_input(self.driver))

    def test6_inputs_incorrect_input(self):
        inputs_page.click_inputs_tabs(self.driver)
        self.assertTrue(inputs_page.send_incorrect_keys_to_input(self.driver))

    def test7_dropdown_select(self):
        dropdown_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_page.dropdown_content_visible(self.driver))
        dropdown_page.get_first_dropdown_value(self.driver)
        sleep(3)

    def test8_add_element(self):
        add_remove_page.click_add_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)

    def test9_delete_element(self):
        add_remove_page.click_add_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)
        add_remove_page.delete_element(self.driver)
        self.assertTrue(add_remove_page.element_invisible(self.driver))

    def test10_date_picker_input_correct_date(self):
        date_picker.click_date_picker(self.driver)
        self.assertTrue(date_picker.date_picker_visible(self.driver))
        self.assertTrue(date_picker.input_correct_date(self.driver))
        sleep(1)

    def test11_date_picker_input_incorrect_date(self):
        date_picker.click_date_picker(self.driver)
        self.assertTrue(date_picker.date_picker_visible(self.driver))
        self.assertTrue(date_picker.input_incorrect_date(self.driver))
        sleep(1)

    def test12_basic_auth_correct(self):
        basic_auth.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth.basic_auth_visible(self.driver))
        self.assertTrue(basic_auth.login_correct(self.driver))
        sleep(2)

    def test13_basic_auth_incorrect_login(self):
        basic_auth.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth.basic_auth_visible(self.driver))
        self.assertTrue(basic_auth.login_incorrect_login(self.driver))
        sleep(2)

    def test14_basic_auth_incorrect_password(self):
        basic_auth.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth.basic_auth_visible(self.driver))
        self.assertTrue(basic_auth.login_incorect_password(self.driver))
        sleep(2)

    def test15_form_submit_correct(self):
        form.click_form_tab(self.driver)
        self.assertTrue(form.form_tab_content(self.driver))
        self.assertTrue(form.form_tab_submit_correct(self.driver))
        sleep(2)

    def test17_key_presses_check(self):
        key_presses.click_key_presses(self.driver)
        self.assertTrue(key_presses.key_presses_visible(self.driver))
        self.assertTrue(key_presses.key_presses_input_value(self.driver))

    def test18_drag_and_drop_check(self):
        drag_and_drop.click_drag_and_drop(self.driver)
        self.assertTrue(drag_and_drop.drag_and_drop_visible(self.driver))
        drag_and_drop.drag_and_drop_correct(self.driver)

    def test19_status_code_200(self):
        status_code.click_status_code(self.driver)
        self.assertTrue(status_code.status_code_visible(self.driver))
        self.assertTrue(status_code.status_code_200_check(self.driver))

    def test20_status_code_305(self):
        status_code.click_status_code(self.driver)
        self.assertTrue(status_code.status_code_visible(self.driver))
        self.assertTrue(status_code.status_code_305_check(self.driver))

    def test21_status_code_404(self):
        status_code.click_status_code(self.driver)
        self.assertTrue(status_code.status_code_visible(self.driver))
        self.assertTrue(status_code.status_code_404_check(self.driver))

    def test22_status_code_500(self):
        status_code.click_status_code(self.driver)
        self.assertTrue(status_code.status_code_visible(self.driver))
        self.assertTrue(status_code.status_code_500_check(self.driver))

    def test23_IFrame_button_1(self):
        IFrame.click_iframe(self.driver)
        self.assertTrue(IFrame.iframe_visible(self.driver))
        self.assertTrue(IFrame.iframe_press_button_1(self.driver))


if __name__ == '__main__':
    unittest.main()

