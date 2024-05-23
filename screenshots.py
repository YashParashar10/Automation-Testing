import time

from selenium import webdriver
driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.wwe.com/")
time.sleep(2)
#driver.save_screenshot("C:\seleniumpractice\ss1.png")
driver.get_screenshot_as_file("C:\seleniumpractice\ss2.jpg")
