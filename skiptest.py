import  unittest
class Apptesting(unittest.TestCase):

    def test_search(self):
        print("This is a search test ")


    @unittest.SkipTest #skips this adv search
    def test_advancesearch(self):
        print("this is adv search method")

    def test_prepaidrecharge(self):
        print("this is prepaid recharge")

    @unittest.skip("skipping this test method because it is not ready")
    def test_postpaidrecharge(self):
        print("this is postpaid recharge")

    def test_loginbygmail(self):
        print("this is login by gmail")


    @unittest.skipIf(1==1,"cuz it is true")
    def test_loginbytwitter(self):
        print("this is login by twitter")


if __name__ == "__main__":
    unittest.main
