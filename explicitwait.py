import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.implicitly_wait(5)  # webdriver syntax
# explicit wait works on the condition not based on time like implicit wait does

driver.maximize_window()

driver.get("https://www.expedia.com/")
driver.find_element_by_id("tab-flight-tab-hp").click() # click on the flights button

time.sleep(2) # python syntax

