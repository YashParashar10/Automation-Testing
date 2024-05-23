from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button[1]').click()
time.sleep(5)
alert = driver.switch_to.alert
alert.accept() # closes popup by clicking on ok button
#alert.dismiss()
time.sleep(2)
