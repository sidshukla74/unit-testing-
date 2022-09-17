from msilib.schema import Class
import unittest
import main

#we are inheritng from unittest
class Problem_Check(unittest.TestCase):


    def test_divide(self):
        val1 = 10
        val2 = 20
        result = main.divide(val1, val2)
        expected = 1
        self.assertEqual(result, expected)


    def test_add(self):
        val1 = 10
        val2 = 20
        result = main.add(val1, val2)
        expected = 30
        self.assertEqual(result, expected)

    def test_sub(self):
        val1 = 20
        val2 = 10
        result = main.sub(val1, val2)
        expected = 10
        self.assertEqual(result, expected)
        

if __name__ == "__main__":
    unittest.main()

