from selenium import webdriver

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

driver.get("http://newtours.demoaut.com/")  # opening URL takes some time
# implicit = all the elements in the application
# wait some time here
driver.implicitly_wait(10)  # seconds specify only 1 time
assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("login").click()
