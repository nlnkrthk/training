import unittest
from app import add,sub,mul

class Testcals(unittest.TestCase):

    def testadd(self):
        self.assertEqual(add(3,3),6)

    def testsub(self):
        self.assertEqual(sub(3,3),6)
    
    def testmul(self):
        self.assertEqual(sub(3,3),6)


if __name__ == "__main__":
    unittest.main()