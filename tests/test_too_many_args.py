from argparse import ArgumentError
import unittest
from calc import aec_subtract, aec_divide

class TestArgs(unittest.TestCase):

    def test_limit_two_args(self):
        # Asserts that an exception is thrown if specified values are passed in
        # If no exception is failed, this assertion will not be true, and the test will fail        
        self.assertRaises(Exception, aec_subtract, [6, 3, 2])

        with self.assertRaises(Exception):
            aec_divide([20, 2, 5, 4])
        
        # ^ this is just another way to format a similar assertion