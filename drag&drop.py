from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
driver = webdriver.Edge()
driver.maximize_window()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
time.sleep(1)
source_element = driver.find_element(By.XPATH,'//*[@id="box6"]')
target_element= driver.find_element(By.XPATH,'//*[@id="box106"]')
action = ActionChains(driver)
action.drag_and_drop(source_element,target_element).perform()
time.sleep(5)
#performmsdraganddrop actions
