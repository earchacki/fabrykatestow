from tests.helpers.support_functions import *

add_remove_tab = 'addremoveelements-header'
add_remove_content = 'addremoveelements-content'
new_element = '//*[@id="addremoveelements-content"]/div/div/button'
added_element = '//*[@id="elements"]/button'


def click_add_remove_tab(driver_instance):
    elem = driver_instance.find_element(By.ID, add_remove_tab)
    elem.click()


def add_remove_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.ID, add_remove_content)
    return elem.is_displayed()


def add_element(driver_instance):
    elem = driver_instance.find_element(By.XPATH, new_element)
    elem.click()


def delete_element(driver_instance):
    elem = driver_instance.find_element(By.XPATH, added_element)
    elem.click()
    wait_for_invisibility_of_element(driver_instance, By.XPATH, added_element)


def element_invisible(driver_instance):
    try:
        wait_for_invisibility_of_element(driver_instance, By.XPATH, added_element)
        return True
    except NoSuchElementException:
        return False
