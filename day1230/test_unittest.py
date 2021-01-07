import unittest


class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUp Class")

    def setUp(self) -> None:
        print("test_setUp")

    def tearDown(self) -> None:
        print("test_tearDown")

    def testOne(self):
        print("test_one")

    def testTwo(self):
        print("testTwo")

    @classmethod
    def tearDownClass(cls) -> None:
        print("testDownClass")


if __name__ == '__main__':
    unittest.main()
