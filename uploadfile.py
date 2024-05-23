from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.find_element(By.ID,'RESULT_FileUpload-10').send_keys("C://Users/Spanidea-LT-103/Downloads/img1.jpg")
time.sleep(2)
