import unittest

def setUpModule(): # will be executed before executing any class or any method present in the test class
    print("setUpModule")

def tearDownModule():
    print("tearDownModule")


class AppTesting(unittest.TestCase):
    # set up method (starting)
    @classmethod
    def setUp(self):  # execute before all test methods
        print("THIS IS LOGIN TEST")

    # teardown method  (ending)
    @classmethod
    def tearDown(self): # execute  after all test methods
        print("This is logout test")



    @classmethod
    def setUpClass(cls):  # execute once when the class started
        print("open app")



    @classmethod
    def tearDownClass(cls): # execute once after  test methods
        print("close application")


    def test_search(self):
        print("search test")
    def test_advancedsearch(self):
        print("this is advanced search")
    def test_perpaidRecharge(self):
        print("This is prepaid recharge test")
    def test_postpaidRecharge(self):
        print("This is post paid recharge test")

if __name__ == "__main__":
    unittest.main()
