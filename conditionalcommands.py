from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

driver.get("https://newtours.demoaut.com")