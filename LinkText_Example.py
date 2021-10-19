from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.selenium.dev/downloads/")
list_anchor_element=driver.find_elements_by_tag_name("a")
#print(list_anchor_element)

for l in list_anchor_element:
    print(l.text)

