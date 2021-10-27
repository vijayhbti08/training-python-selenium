from selenium import webdriver

cap={'browserName': 'chrome', 'platform': 'ANY', 'version': ''}

driver = webdriver.Remote(command_executor='http://192.168.89.61:4444/wd/hub',desired_capabilities=cap)
driver.get("https://www.google.com")
print("Title:::"+driver.title)
driver.close()
