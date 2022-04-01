from tests.helpers.support_functions import *
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

drag_and_drop_tab = 'draganddrop-header'
drag_and_drop_content = 'draganddrop-content'
column_a = 'column-a'
column_b = 'column-b'
header_a = '//*[@id="column-a"]/header'
header_b = '//*[@id="column-b"]/header'


def click_drag_and_drop(driver_instance):
    elem = driver_instance.find_element(By.ID, drag_and_drop_tab)
    elem.click()


def drag_and_drop_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.ID, drag_and_drop_content)
    return elem.is_displayed()


def drag_and_drop_correct(driver_instance):
    elem = driver_instance.find_element(By.ID, column_a)
    elem1 = driver_instance.find_element(By.ID, column_b)
    action = ActionChains(driver_instance)
    #action.drag_and_drop_by_offset(elem, 100, 100).perform()
    #action.drag_and_drop(elem, elem1).perform()
    action.click_and_hold(elem).move_by_offset(200, 10).pause(2).release().perform()
    sleep(2)

