from time import sleep

from selenium import webdriver


driver=webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("testing frame")
driver.switch_to.default_content()
