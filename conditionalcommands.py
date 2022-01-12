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

user_ele.send_keys("mercury")
pw_ele.send_keys("mercury")

driver.find_element_by_name("login").click()

roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
print("status of round trip radio button", roundtrip_radio.is_selected()) #print status of radio button round trip

onetrip_radio = driver.find_element_by_css_selector("input[value=oneway]")

print("status of one way radio button", onetrip_radio.is_selected())