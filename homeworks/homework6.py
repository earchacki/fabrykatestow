from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

url = 'https://fabrykatestow.pl/'

xpath = '/html/body/div/main/div/div/div/div/div/div/div/section[6]/div[2]/div/div/div/div/section/div/div/div[1]/div/div'
path_to_save_screenshot = 'C:/Temp/screenshot6.png'


driver = webdriver.Chrome('C:/Users/emil.archacki/PycharmProjects/seleniumWebdriverGit/chromedriver.exe')
driver.maximize_window()
driver.get(url)
time.sleep(1)

def hover_over_element(driver, xpath):
    elem = driver.find_element(By.XPATH, xpath)
    hover = ActionChains(driver).move_to_element(elem)
    hover.perform()

element = driver.find_element(By.XPATH, '/html/body/div/header/div/nav[1]/div/div/div/div[2]/div/div/div/ul/li[2]/a')
element.click()
time.sleep(1)

element = driver.find_element(By.XPATH, '/html/body/div/main/div/div/div/section[5]/div/div/div/div[2]/div/section[1]/div/div/div[1]/div/div/div/div/div/a')
element.click()
time.sleep(1)

hover_over_element(driver, xpath)
driver.save_screenshot(path_to_save_screenshot)

driver.quit()

