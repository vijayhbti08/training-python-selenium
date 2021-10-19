from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
wait = WebDriverWait(driver, 20)  # Explicit wait
driver.find_element_by_xpath("//div[@id='login_button_container']/div/form/div/input[@type='text']").send_keys(
    "standard_user")
driver.find_element_by_xpath("//div[@id='login_button_container']/div/form/div/input[@type='password']").send_keys(
    "secret_sauce")

driver.find_element_by_xpath("//div[@id='login_button_container']/div/form/input").click()
wait.until(EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))
driver.find_element_by_id("add-to-cart-sauce-labs-backpack").click()
wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), '1'))
print(driver.find_element_by_class_name("shopping_cart_badge").text)
driver.quit()
