import unittest

from app.calculator import add


class TestStringCalculator(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(add(""), 0)
    

    def test_single_number(self):
        self.assertEqual(add("1"), 1)
        self.assertEqual(add("2"), 2)
    

    def test_two_numbers(self):
        self.assertEqual(add("1,2"), 3)
        self.assertEqual(add("10,20"), 30)
    

    def test_ignore_empty_strings(self):
        self.assertEqual(add("1,"), 1)
        self.assertEqual(add(",2"), 2)
        self.assertEqual(add(","), 0)


if __name__ == "__main__":
    unittest.main()

