import unittest
class Test(unittest.TestCase):
    def testName(self):
       # self.assertLess(100,100)
        self.assertLessEqual(100,500)
        #self.assertGreaterEqual(100,100)
        #self.assertGreater(100,10)
if __name__ ==  "__main__":
    unittest.main()

