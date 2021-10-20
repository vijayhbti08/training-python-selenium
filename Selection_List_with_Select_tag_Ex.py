from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")
element = driver.find_element_by_id("withOptGroup")
element.click()
sleep(4)

action = ActionChains(driver)
action.move_to_element(element).send_keys(Keys.DOWN).send_keys(Keys.DOWN).send_keys(Keys.RETURN).perform()
