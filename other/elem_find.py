# _*_encoding:utf-8_*_

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

elem = driver.find_element_by_id("wrapper")
elem2 = elem.find_element_by_id("u")
elem3 = elem2.find_elements_by_tag_name("a")
print len(elem3)