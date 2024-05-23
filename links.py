from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver= webdriver.Edge()
driver.maximize_window()
driver.get("http://google.com/")
links= driver.find_elements(By.TAG_NAME,"a")
print("No of links present",len(links)) # prints no of links present in the page

for link in links:
    print(link.text)

# click on the link
driver.find_element(By.LINK_TEXT,"Sign in").click()
