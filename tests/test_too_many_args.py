from argparse import ArgumentError
import unittest
from calc import aec_subtract, aec_divide

class TestArgs(unittest.TestCase):

    def test_limit_two_args(self):
        self.assertRaises(Exception, aec_subtract, [6, 3, 2])
        self.assertRaises(Exception, aec_divide, [20, 2, 5, 4])