from itertools import dropwhile
from time import sleep

from selenium import webdriver


driver=webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/nested_frames")
driver.switch_to.frame(0)
driver.switch_to.frame("frame-left")
print(driver.find_element_by_xpath("/html/body").text)
driver.switch_to.default_content()