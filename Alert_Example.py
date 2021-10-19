from time import sleep

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/javascript_alerts")
driver.find_element_by_xpath("//button[contains(text(),'Click for JS Alert')]").click()
sleep(6)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()   #clicking on ok button in alert


driver.find_element_by_xpath("//button[contains(text(),'Click for JS Confirm')]").click()
sleep(6)
alert = driver.switch_to.alert
print("2nd alert::{}".format(alert.text))
alert.dismiss()


driver.find_element_by_xpath("//button[contains(text(),'Click for JS Prompt')]").click()
sleep(6)
alert = driver.switch_to.alert
print("3rd alert::{}".format(alert.text))
alert.send_keys("This is Python selenium class")
alert.accept()