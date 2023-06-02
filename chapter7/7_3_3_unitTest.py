import unittest
import numpy as np

class TestRoot(unittest.TestCase):
    def test_root(self):
        # np.roots([a,b,c]) solves the function ax^2+bx+c=0
        roots = list(np.roots([1,1,-2]))
        my_answer = [-2.0,1.0]
        self.assertEqual(my_answer, roots)

unittest.main()