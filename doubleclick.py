from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

Element = driver.find_element(By.XPATH,'//*[@id="HTML10"]/div[1]/button')
actions= ActionChains(driver)
actions.double_click(Element).perform() #double clicks
time.sleep(2)
