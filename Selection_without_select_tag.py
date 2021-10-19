from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")

element=driver.find_element_by_id("withOptGroup")
element.click()
sleep(5)
driver.find_element_by_id("react-select-2-option-0-1").click()
sleep(5)

driver.close()