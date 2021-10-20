from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://demoqa.com/droppable")
wait = WebDriverWait(driver, 20)
driver.maximize_window()
action = ActionChains(driver)  # keyboard and mouse operation

element_a = driver.find_element_by_id("draggable")
element_b = driver.find_element_by_id("droppable")
print("perform operation")
action.drag_and_drop(element_a, element_b).perform()
print(action.drag_and_drop(element_a, element_b))
print("performed operation")
sleep(4)
driver.close()
