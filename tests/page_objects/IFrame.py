from tests.helpers.support_functions import *
from time import sleep

IFrame_tab = 'iframe-header'
IFrame_content = 'iframe-content'
button_1 = 'simpleButton1'
button_2 = 'simpleButton2'
which_button_is_clicked = 'whichButtonIsClickedMessage'

def click_iframe(driver_instance):
    elem = driver_instance.find_element(By.ID, IFrame_tab)
    elem.click()


def iframe_visible(driver_instance):
    driver_instance.switch_to.frame(0)
    elem = wait_for_visibility_of_element(driver_instance, By.ID, button_1)
    return elem.is_displayed()


def iframe_press_button_1(driver_instance):
    elem = driver_instance.find_element(By.ID, button_1)
    elem.click()
    elem1 = driver_instance.find_element(By.ID, which_button_is_clicked)
    expected_value = 'Button 1 was clicked!'
    sleep(2)
    if elem1.text == expected_value:
        return True
    else:
        return False

