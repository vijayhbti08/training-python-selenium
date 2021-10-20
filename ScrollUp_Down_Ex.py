from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/documentation/")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(5)
# driver.execute_script("window.scrollTo(0, -500);")

