from tests.helpers.support_functions import *
from datetime import datetime
from time import sleep

date_picker_tab = 'datepicker-header'
date_picker_content = 'datepicker-content'
date_input = '//*[@id="start"]'


def click_date_picker(driver_instance):
    elem = driver_instance.find_element(By.ID, date_picker_tab)
    elem.click()


def date_picker_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.ID, date_picker_content)
    return elem.is_displayed()


def input_correct_date(driver_instance):
    elem = driver_instance.find_element(By.XPATH, date_input)
    elem.click()
    value = '04.12'
    elem.send_keys(value)
    elem1 = datetime.strptime(elem.get_attribute('value'), '%Y-%m-%d').strftime('%d.%m.%Y')
    if value + '.2020' == elem1:
        return True
    else:
        return False


def input_incorrect_date(driver_instance):
    elem = driver_instance.find_element(By.XPATH, date_input)
    elem.click()
    value = '67.12'
    elem.send_keys(value)
    sleep(2)
    elem1 = datetime.strptime(elem.get_attribute('value'), '%Y-%m-%d').strftime('%d.%m.%Y')
    if value + '.2020' == elem1:
        return False
    else:
        return True






