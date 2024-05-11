import unittest
from Q1 import getMinimumDifference
from ed_utils.decorators import number
from tests.conversions import toBST

class Test_Q1(unittest.TestCase):
    @number("1.1")
    def test_examples(self):
        self.assertEqual(getMinimumDifference(toBST([4,2,6,1,3])), 1)
        self.assertEqual(getMinimumDifference(toBST([236,104,701,227,911])), 9)

    @number("1.2")
    def test_extra(self):
        self.assertEqual(getMinimumDifference(toBST([1,0,48,12,49])), 1)


if __name__ == '__main__':
    unittest.main()