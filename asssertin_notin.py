import unittest
from selenium import webdriver
class Test(unittest.TestCase):
    def testName(self):
        list = {"py","sel","jav"}
        self.assertNotIn("ruby",list)
       # self.assertIn("py",list)
if __name__ == "__main__":
    unittest.main()
