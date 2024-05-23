from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://wwe.com")
print(driver.title)
time.sleep(5)
driver.get("https://wikipedia.com")
print(driver.title)
time.sleep(5)
driver.back()
print(driver.title)
time.sleep(5)
driver.forward()
print(driver.title)
