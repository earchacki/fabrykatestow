from tests.helpers.support_functions import *
from time import sleep

status_code_200_xpath = '/html/body/pre'
status_code_305_xpath = '/html/body/pre'
status_code_404_xpath = '/html/body/pre'
status_code_500_xpath = '/html/body/pre'


def status_code_200_check(driver_instance):
    elem = driver_instance.find_element(By.XPATH, status_code_200_xpath)
    expected_value = '200 OK'
    if elem.text == expected_value:
        return True
    else:
        return False


def status_code_305_check(driver_instance):
    elem = driver_instance.find_element(By.XPATH, status_code_305_xpath)
    expected_value = '305 Use Proxy'
    if elem.text == expected_value:
        return True
    else:
        return False


def status_code_404_check(driver_instance):
    elem = driver_instance.find_element(By.XPATH, status_code_404_xpath)
    expected_value = '404 Not Found'
    if elem.text == expected_value:
        return True
    else:
        return False


def status_code_500_check(driver_instance):
    elem = driver_instance.find_element(By.XPATH, status_code_500_xpath)
    expected_value = '500 Internal Server Error'
    if elem.text == expected_value:
        return True
    else:
        return False
