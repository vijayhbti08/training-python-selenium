from time import sleep

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.selenium.dev/")
link_text_element=driver.find_element_by_link_text("Projects")
print(link_text_element.text)
link_text_element.click()

sleep(5)

driver.close()