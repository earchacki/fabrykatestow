from tests.helpers.support_functions import *
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import os

drag_and_drop_tab = 'draganddrop-header'
drag_and_drop_content = 'draganddrop-content'
column_a = 'column-a'
column_b = 'column-b'
header_a = '//*[@id="column-a"]/header'
header_b = '//*[@id="column-b"]/header'


def click_drag_and_drop(driver_instance):
    elem = driver_instance.find_element(By.ID, drag_and_drop_tab)
    elem.click()


def drag_and_drop_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.ID, drag_and_drop_content)
    return elem.is_displayed()


def drag_and_drop_correct(driver_instance):
    base_path = os.path.abspath('page_test.py')
    helpers_dir_path = base_path.replace('tests_run\page_test.py', 'helpers\drag_and_drop_helper.js')
    with open(helpers_dir_path, 'r') as js_file:
        line = js_file.readline()
        script = ''
        while line:
            script += line
            line = js_file.readline()

    driver_instance.execute_script(script + "jQuery('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")
    elem = driver_instance.find_element(By.XPATH, header_a)
    elem1 = driver_instance.find_element(By.XPATH, header_b)
    if elem.text == 'B' and elem1.text == 'A':
        return True
    else:
        return False

