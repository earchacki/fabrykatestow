from tests.helpers.support_functions import *

input_tab = 'inputs-header'
input_content = 'inputs-content'
input = '//*[@id="inputs-content"]/div/input'


def click_inputs_tabs(driver_instance):
    elem = driver_instance.find_element(By.ID, input_tab)
    elem.click()


def input_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.ID, input_content)
    return elem.is_displayed()


def send_correct_keys_to_input(driver_instance):
    wait_for_visibility_of_element(driver_instance, By.XPATH, input)
    elem = driver_instance.find_element(By.XPATH, input)
    elem.send_keys('123456')
    value = 123456
    if value == int(elem.get_attribute('value')):
        return True
    else:
        return False


def send_incorrect_keys_to_input(driver_instance):
    wait_for_visibility_of_element(driver_instance, By.XPATH, input)
    elem = driver_instance.find_element(By.XPATH, input)
    elem.send_keys('abc')
    value = 'abc'
    if value == elem.get_attribute('value'):
        return False
    else:
        return True
