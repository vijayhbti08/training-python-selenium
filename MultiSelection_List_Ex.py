from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")

selection_element=driver.find_element_by_id("cars")
select=Select(selection_element)
print(select.is_multiple)
select.select_by_index(3)     #Audi will be selected
sleep(4)


select.select_by_value("saab")   #Saab will be selected
sleep(4)
all_selected_option=select.all_selected_options

for l in all_selected_option:
    if l.text == 'Saab':
        print("Saab is selected successfully")
        break
driver.close()
