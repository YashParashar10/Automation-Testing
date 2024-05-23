from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.edge.options import Options
edgeOptions = Options()

edgeOptions.add_experimental_option("prefs",{"download.default_directory":"C:\Downloadedfiles"})
driver = webdriver.Edge(edge_options=edgeOptions)
driver.maximize_window()
#download text file
#driver.get("https://demo.automationtesting.in/FileDownload.html/")
'''' driver.find_element(By.ID,'textbox').send_keys("demo text")
 driver.find_element(By.XPATH,'create text').click()
 driver.find_element(By.ID,'link-to-download').click() '''
# we set preferences if we use firefox browser and handle the download functionality according to the window



