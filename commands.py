from selenium import webdriver
# from selenium.web driver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
import time

# Chrome
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get("https://www.google.com")
print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath('//*[@id="gb"]/div/div[1]/div/div[1]/a').click()
time.sleep(3)
#driver.close() #closes current browser in focus
driver.quit() #closes all browsers, child and parent