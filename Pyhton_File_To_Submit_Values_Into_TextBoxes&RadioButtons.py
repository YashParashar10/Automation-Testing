from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver= webdriver.Edge()
driver.maximize_window()

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
# count the number of text input in a website by targeting the class attribute
inputboxes=driver.find_elements(By.CLASS_NAME,'form-control')
print((len(inputboxes)))



# how to add value in the text input boxes
#driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH,'//*[@id="contact_form"]/fieldset/div[1]/div/div/input').send_keys("yash")
driver.find_element(By.XPATH,'//*[@id="contact_form"]/fieldset/div[2]/div/div/input').send_keys("parashar")
driver.find_element(By.XPATH, '//*[@id="contact_form"]/fieldset/div[4]/div/div/input').send_keys("1234567890")
driver.find_element(By.XPATH, '//*[@id="contact_form"]/fieldset/div[3]/div/div/input').send_keys("abc1@gmail.com")
driver.find_element(By.XPATH, '//*[@id="contact_form"]/fieldset/div[5]/div/div/input').send_keys(" B-10 , Sardarpura ,Jodhpur")
driver.find_element(By.XPATH, '//*[@id="contact_form"]/fieldset/div[6]/div/div/input').send_keys(" Jodhpur")
driver.find_element(By.XPATH, '//*[@id="contact_form"]/fieldset/div[7]/div/div/select').send_keys("Texas")
driver.find_element(By.XPATH, '//*[@id="contact_form"]/fieldset/div[8]/div/div/input').send_keys("34298")
driver.find_element(By.XPATH, '//*[@id="contact_form"]/fieldset/div[9]/div/div/input').send_keys("www.google.com")
driver.find_element(By.XPATH, '//*[@id="contact_form"]/fieldset/div[10]/div/div[1]/label/input').click()
driver.find_element(By.XPATH, '//*[@id="contact_form"]/fieldset/div[11]/div/div/textarea').send_keys("Beginning the automation testing skill")




time.sleep(4)

#how to get the staus of the input boxes

Status = driver.find_element(By.XPATH,'//*[@id="contact_form"]/fieldset/div[1]/div/div/input').is_displayed()
print(Status)
