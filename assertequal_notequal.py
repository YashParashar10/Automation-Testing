import unittest
from selenium import webdriver
class Test (unittest.TestCase):
    def testName(self):
        driver = webdriver.Edge()
        driver.get("https://www.google.com")
        title_webpage = driver.title
        #self.assertEqual("Google",title_webpage,"webpage title is not same")
       # self.assertEqual("Firefox", title_webpage, "webpage title is not same")
        self.assertNotEqual("Googl12e",title_webpage)

if __name__ == "__main__":
    unittest.main()

