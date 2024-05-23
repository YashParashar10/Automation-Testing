from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
VAR =driver.find_element(By.XPATH,'/html/body/div/section/div/div/div/p/span')
actions = ActionChains(driver)
actions.context_click(VAR).perform() #right click action
time.sleep(4)
