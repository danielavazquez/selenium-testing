from selenium import webdriver

chromedriver = '/usr/local/bin/chromedriver'
browser = webdriver.Chrome(chromedriver)
browser.get('https://stackoverflow.com/users/login')
print(browser.title)
print(browser.current_url)
#print(browser.page_source)
browser.close()
