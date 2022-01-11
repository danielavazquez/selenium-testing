import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

driver.get("http://newtours.demoaut.com/")
print(driver.title) #FR
driver.get("http://pavantestingtools.blogspot.in/")
time.sleep(3)
print(driver.title) #tt
driver.back()
time.sleep(3)
print(driver.title) #FR
driver.forward()
print(driver.title) #tt
driver.quit()