import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        #driver = webdriver.Edge()
        driver = None
        self.assertIsNotNone(driver)
        #driver.maximize_window()
        self.assertIsNone(driver)
if __name__ =="__main__":
    unittest.main()

