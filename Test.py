import unittest

from add import summation

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [20, 5]
        result = summation(data)
        self.assertEqual(result, 25)

if __name__ == '__main__':
    unittest.main()
