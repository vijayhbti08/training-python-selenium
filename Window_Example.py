from time import sleep

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")

parent_widnow=driver.current_window_handle
print("parent window handle::{}".format(parent_widnow))

driver.find_element_by_link_text("Click Here").click()
sleep(5)

window_handle_list = driver.window_handles
print(window_handle_list)
for handle in window_handle_list:
    driver.switch_to.window(handle)
    if driver.title == 'New Window':
        print(driver.title)
        driver.close()
driver.switch_to.window(parent_widnow)
print("After closing child window::{}".format(driver.title))

