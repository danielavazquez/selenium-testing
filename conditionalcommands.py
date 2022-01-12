from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

driver.get("https://www.discover.com/")

user_ele = driver.find_element_by_name("userID")
print(user_ele.is_displayed())  # returns true/false based upon status of element
print(user_ele.is_enabled())  # also returns true/false based upon status of element

pw_ele = driver.find_element_by_name("password")
print(pw_ele.is_displayed())
print(pw_ele.is_enabled())
