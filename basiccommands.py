from selenium import webdriver
import time

from selenium.webdriver.chrome.webdriver import WebDriver

driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get('http:www.amazon.com')
print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath('//*[@id="nav-global-location-popover-link"]').click()
time.sleep(5)
driver.close()