from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get('http:www.google.com')
print(driver.title)
print(driver.current_url)

driver.close()