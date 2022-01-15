import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.implicitly_wait(5)  # webdriver syntax
# explicit wait works on the condition not based on time like implicit wait does

driver.maximize_window()

driver.get("https://www.expedia.com/")
driver.find_element_by_id("tab-flight-tab-hp").click() # click on the flights button
driver.find_element_by_id("flight-origin-hp-flight").send_keys("SFO") # origin

time.sleep(2) # python syntax

driver.find_element_by_id("flight-destination-hp-flight").send_keys("NYC") # destination

driver.find_element_by_id("flight-destination-hp-flight").clear()
driver.find_element_by_id("flight-departing-hp-flight").send_keys("12/10/2018")

driver.find_element_by_id("flight-returning-hp-flight").clear()
driver.find_element_by_id("flight-returning-hp-flight").send_keys("15/10/2018")

driver.find_element_by_xpath('//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button').click()