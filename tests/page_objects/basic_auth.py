from tests.helpers.support_functions import *
from tests.page_objects.logged_in_page import *

basic_auth_tab = 'basicauth-header'
basic_auth_content = 'basicauth-content'
input_username = 'ba_username'
input_password = 'ba_password'
button_login = '//*[@id="content"]/button'
message_invalid_credentials = 'loginFormMessage'


def click_basic_auth_tab(driver_instance):
    elem = driver_instance.find_element(By.ID, basic_auth_tab)
    elem.click()


def basic_auth_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.ID, basic_auth_content)
    return elem.is_displayed()


def login_correct(driver_instance):
    login = 'admin'
    password = 'admin'
    elem = driver_instance.find_element(By.ID, input_username)
    elem.send_keys(login)
    elem1 = driver_instance.find_element(By.ID, input_password)
    elem1.send_keys(password)
    elem2 = driver_instance.find_element(By.XPATH, button_login)
    elem2.click()
    elem3 = logged_in_check(driver_instance)
    return elem3


def login_incorrect_login(driver_instance):
    login = 'wrong_admin'
    password = 'admin'
    elem = driver_instance.find_element(By.ID, input_username)
    elem.send_keys(login)
    elem1 = driver_instance.find_element(By.ID, input_password)
    elem1.send_keys(password)
    elem2 = driver_instance.find_element(By.XPATH, button_login)
    elem2.click()
    try:
        elem3 = driver_instance.find_element(By.ID, message_invalid_credentials)
        if elem3.text == 'Invalid credentials':
            return True
        else:
            return False
    except NoSuchElementException:
        return False


def login_incorect_password(driver_instance):
    login = 'admin'
    password = 'wrong_password'
    elem = driver_instance.find_element(By.ID, input_username)
    elem.send_keys(login)
    elem1 = driver_instance.find_element(By.ID, input_password)
    elem1.send_keys(password)
    elem2 = driver_instance.find_element(By.XPATH, button_login)
    elem2.click()
    try:
        elem3 = driver_instance.find_element(By.ID, message_invalid_credentials)
        if elem3.text == 'Invalid credentials':
            return True
        else:
            return False
    except NoSuchElementException:
        return False


