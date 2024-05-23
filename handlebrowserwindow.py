from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element(By.XPATH,'//*[@id="Tabbed"]/a/button').click()
time.sleep(2)
print( driver.current_window_handle) #parent window
handles= driver.window_handles # return all the values of opened values

for handle in handles:
    driver._switch_to.window(handle)
    print(driver.title)
    if driver.title=="Frames & windows":
        driver.close()
time.sleep(2)
driver.quit()
