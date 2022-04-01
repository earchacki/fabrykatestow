from tests.helpers.support_functions import *

form_tab = 'form-header'
form_content = 'form-content'
input_first_name = 'fname'
input_last_name = 'lname'
button_submit = 'formSubmitButton'

def click_form_tab(driver_instance):
    elem = driver_instance.find_element(By.ID, form_tab)
    elem.click()


def form_tab_content(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.ID, form_content)
    return elem.is_displayed()


def form_tab_submit_correct(driver_instance):
    first_name = 'Roman'
    last_name = 'Romanowski'
    elem = driver_instance.find_element(By.ID, input_first_name)
    elem.send_keys(first_name)
    elem1 = driver_instance.find_element(By.ID, input_last_name)
    elem1.send_keys(last_name)
    elem2 = driver_instance.find_element(By.ID, button_submit)
    elem2.click()
    return True
