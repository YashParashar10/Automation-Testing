import time

from selenium.webdriver.common.by import By
import utliltyfordatadriventestcase
from selenium import webdriver
import time
driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
path = "C:\\Users\Spanidea-LT-103\Desktop\YASHSPANIDEA\datadriven.xlsx"

rows = utliltyfordatadriventestcase.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
     username = utliltyfordatadriventestcase.readData(path,"Sheet1",r,1)
     password = utliltyfordatadriventestcase.readData(path,"Sheet1",r,2)

     driver.find_element(By.NAME,'username').send_keys(username)
     driver.find_element(By.NAME, 'password').send_keys(password)

     driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
     time.sleep(2)

      if driver.title == "OrangeHRM":
         print("test case passed")
         utliltyfordatadriventestcase.writeData(path,"Sheet1",r,3,"Test Passed")
         time.sleep(2)
     else:
         print("test case failed")
         utliltyfordatadriventestcase.writeData(path, "Sheet1", r, 3, "Test Failed")
         time.sleep(3)
     driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p').click()
     driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()
