from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Edge driver
driver = webdriver.Edge()
driver.maximize_window()

# Open the target URL
driver.get("https://www.worldometers.info/geography/alphabetical-list-of-countries/")

# Scroll down the page by 1000 pixels
#driver.execute_script("window.scrollBy(0, 1000)","")

# Optionally, wait for a few seconds to see the effect of the scroll
# scroll down to the particular element
#var = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr[144]/td[2]')
#driver.execute_script("arguments[0].scrollIntoView();",var)
# scroll till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")
time.sleep(5)

# Close the browser
driver.quit()
