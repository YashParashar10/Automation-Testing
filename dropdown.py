from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.select import Select

driver= webdriver.Edge()
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
element = driver.find_element(By.XPATH,'//*[@id="RESULT_RadioButton-9"]')
drp = Select(element)
all_options = drp.options
for options in all_options:
    print(options.text)
print(len(drp.options)) # gives count of number of options
drp.select_by_visible_text('Morning')
#drp.select_by_value("Radio-2")
#drp.select_by_index(2)
time.sleep(5)
