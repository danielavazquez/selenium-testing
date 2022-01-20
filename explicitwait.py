import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.implicitly_wait(5)  # webdriver syntax
# explicit wait works on the condition not based on time like implicit wait does

driver.maximize_window()

driver.get("http://demo.guru99.com/test/newtours/")
driver.find_element_by_id("tab-flight-tab-hp").click() # click on the flights button
driver.find_element_by_id("flight-origin-hp-flight").send_keys("SFO") # origin

time.sleep(2) # python syntax

driver.find_element_by_id("flight-destination-hp-flight").send_keys("NYC") # destination

driver.find_element_by_id("flight-destination-hp-flight").clear()
driver.find_element_by_id("flight-departing-hp-flight").send_keys("12/10/2018")

driver.find_element_by_id("flight-returning-hp-flight").clear()
driver.find_element_by_id("flight-returning-hp-flight").send_keys("15/10/2018")

driver.find_element_by_xpath('//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button').click()

wait = WebDriverWait(driver,10)

wait.until(EC.element_to_be_clickable((driver.find_element_by_xpath('//*[@id='stopFilter_stops-0']')))



