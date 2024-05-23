from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the target URL
driver.get("https://demo.nopcommerce.com/")

# Locate the element using class name
ele = driver.find_element(By.CLASS_NAME, "q")
print(ele.is_displayed())  # return t/f based on elements status
print(ele.is_enabled())
