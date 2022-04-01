from tests.helpers.support_functions import *
from selenium.webdriver.common.keys import Keys
from time import sleep

key_presses_tab = 'keypresses-header'
key_presses_content = 'keypresses-content'
key_presses_input = 'target'
key_presses_value = 'keyPressResult'


def click_key_presses(driver_instance):
    elem = driver_instance.find_element(By.ID, key_presses_tab)
    elem.click()


def key_presses_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.ID, key_presses_content)
    return elem.is_displayed()


def key_presses_input_value(driver_instance):
    elem = driver_instance.find_element(By.ID, key_presses_input)
    elem.send_keys(Keys.ENTER)
    sleep(2)
    elem1 = driver_instance.find_element(By.ID, key_presses_value)
    print(elem1.text)
    if elem1.text == 'You entered: ENTER':
        return True
    else:
        return False