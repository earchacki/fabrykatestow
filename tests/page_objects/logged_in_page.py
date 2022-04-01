from tests.helpers.support_functions import *

logged_in_message = 'loggedInMessage'
button_return = 'retrun button'


def logged_in_check(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.ID, logged_in_message)
    return elem.is_displayed()


def return_to_main_page(driver_instance):
    elem = driver_instance.find_element(By.ID, button_return)
    elem.click()