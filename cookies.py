from selenium import webdriver
driver = webdriver.Edge()
driver.get("https://www.amazon.in")
driver.maximize_window()
# capture all the cookies
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
# add new cookie to browser
cookie = {'name':'Mycookie','value':'123456789'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies)) # after adding new cookie
print(cookies) # total cookies

# delete coookie
driver.delete_cookie('Mycookie')
cookies = driver.get_cookies()
print(len(cookies)) # after deleting cookie
print(cookies)

#delete all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
