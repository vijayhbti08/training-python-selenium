from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")

selection_element=driver.find_element_by_id("oldSelectMenu")
select=Select(selection_element)
select.select_by_index(3)     #Yellow will be selected
sleep(4)
selected_value=select.first_selected_option
assert selected_value.text in "Yellow"
select.select_by_value("8")   #indigo will be selected
sleep(4)
select.select_by_visible_text("Magenta")   #Magenta will be selected
sleep(4)
driver.close()
