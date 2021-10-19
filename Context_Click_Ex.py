from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/context_menu")
wait=WebDriverWait(driver,20)
action = ActionChains(driver) #keyboard and mouse operation

element = driver.find_element_by_id("hot-spot")
action.context_click(element).perform()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()
sleep(6)