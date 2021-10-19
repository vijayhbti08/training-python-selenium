from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/hovers")
wait=WebDriverWait(driver,20)
action = ActionChains(driver) #keyboard and mouse operation
userprofile1 = driver.find_element_by_xpath("//body/div[2]/div[1]/div[1]/div[1]/img[1]")
action.move_to_element(userprofile1).perform()
sleep(3)

userprofile2 = driver.find_element_by_xpath("//body/div[2]/div[1]/div[1]/div[2]/img[1]")
action.move_to_element(userprofile2).perform()
sleep(3)

userprofile3 = driver.find_element_by_xpath("//body/div[2]/div[1]/div[1]/div[3]/img[1]")
action.move_to_element(userprofile3).perform()
wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "View profile")))
driver.find_element_by_link_text("View profile").click()
