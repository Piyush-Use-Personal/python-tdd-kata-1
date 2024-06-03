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
    

    def test_multiple_numbers(self):
        self.assertEqual(add("1,2,3"), 6)
        self.assertEqual(add("10,20,30,40,50"), 150)
        self.assertEqual(add("100,200,300,400,500,600"), 2100)


    def test_numbers_with_whitespace(self):
        self.assertEqual(add("1, 2, 3"), 6)
        self.assertEqual(add("10,   20,  30"), 60)
        self.assertEqual(add("100,  200,   300,   400"), 1000)


    def test_newline_between_numbers(self):
        self.assertEqual(add("1\n2,3"), 6)
        self.assertEqual(add("100\n200\n300,400,500\n600"), 2100)

    def test_newline_at_end(self):
        self.assertEqual(add("1\n"), 1)
        self.assertEqual(add("1\n2\n"), 3)
        self.assertEqual(add("100\n200\n300\n"), 600)


if __name__ == "__main__":
    unittest.main()

