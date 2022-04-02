from tests.helpers.support_functions import *
from selenium.webdriver.common.alert import Alert
from time import sleep

form_tab = 'form-header'
form_content = 'form-content'
input_first_name = 'fname'
input_last_name = 'lname'
button_submit = 'formSubmitButton'


def click_form_tab(driver_instance):
    elem = driver_instance.find_element(By.ID, form_tab)
    elem.click()


def form_tab_visible(driver_instance):
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
    # popup = driver_instance.switch_to.alert
    popup = Alert(driver_instance)
    message = 'success'
    if popup.text == message:
        popup.accept()
        return True
    else:
        return False


def form_tab_submit_incorrect(driver_instance):
    elem = driver_instance.find_element(By.ID, button_submit)
    sleep(1)
    elem.click()
    sleep(1)
    message = driver_instance.switch_to.active_element.get_attribute('text')
    print(message)
    value = 'Wypełnij to pole.'
    if message == value:
        return True
    else:
        return False

