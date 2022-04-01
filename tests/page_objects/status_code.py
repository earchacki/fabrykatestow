from tests.helpers.support_functions import *
from time import sleep
from tests.page_objects import status_code_pages

status_code_tab = 'statuscodes-header'
# status_code_content = 'statuscodes-content'
status_200 = '200siteAnchor'
status_305 = '305siteAnchor'
status_404 = '404siteAnchor'
status_500 = '500siteAnchor'

def click_status_code(driver_instance):
    elem = driver_instance.find_element(By.ID, status_code_tab)
    elem.click()


def status_code_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.ID, status_200)
    return elem.is_displayed()


def status_code_200_check(driver_instance):
    elem = driver_instance.find_element(By.ID, status_200)
    elem.click()
    elem1 = status_code_pages.status_code_200_check(driver_instance)
    return elem1


def status_code_305_check(driver_instance):
    elem = driver_instance.find_element(By.ID, status_305)
    elem.click()
    elem1 = status_code_pages.status_code_305_check(driver_instance)
    return elem1


def status_code_404_check(driver_instance):
    elem = driver_instance.find_element(By.ID, status_404)
    elem.click()
    elem1 = status_code_pages.status_code_404_check(driver_instance)
    return elem1


def status_code_500_check(driver_instance):
    elem = driver_instance.find_element(By.ID, status_500)
    elem.click()
    elem1 = status_code_pages.status_code_500_check(driver_instance)
    return elem1
