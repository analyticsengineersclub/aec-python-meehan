import unittest
from calc import aec_subtract # from calc.py

class TestSubtract(unittest.TestCase): # Test class → this is the "wrapper" to wrap up all the test functions

    def test_subtract(self):  # Test function (need 'test_' prefix to tell the framework that this function is part of the test suite)
        arg_ints = [20, 5] # Test data
        sub_result = aec_subtract(arg_ints)  # Apply a function
        self.assertEqual(sub_result, 15) # Asserts that the function above produces the expected result (20 - 5 = 15)
    
# If this test is run as a script (ie. 'python test_subtract.py'), execute the given tasks
if __name__ == "__main__": 
    unittest.main()