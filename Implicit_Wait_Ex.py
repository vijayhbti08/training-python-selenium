from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//div[@id='login_button_container']/div/form/div/input[@type='text']").send_keys("standard_user")
driver.find_element_by_xpath("//div[@id='login_button_container']/div/form/div/input[@type='password']").send_keys("secret_sauce")

driver.find_element_by_xpath("//div[@id='login_button_container']/div/form/input").click()
driver.find_element_by_id("add-to-cart-sauce-labs-backpack").click()