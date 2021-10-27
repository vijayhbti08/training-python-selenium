from selenium import webdriver

profile = webdriver.ChromeOptions()
profile.headless = True


driver = webdriver.Chrome(options=profile)
driver.get("https://www.google.com")
print(driver.title)
driver.close()