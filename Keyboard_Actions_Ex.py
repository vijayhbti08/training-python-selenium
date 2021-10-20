from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/key_presses?")
wait=WebDriverWait(driver,20)
action = ActionChains(driver) #keyboard and mouse operation
action.send_keys(Keys.ENTER).perform()
sleep(5)
