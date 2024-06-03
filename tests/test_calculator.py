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

    def test_custom_delimiter(self):
        self.assertEqual(add("//|\n1|2\n3"), 6)
        self.assertEqual(add("//;\n1;2\n3"), 6)
        self.assertEqual(add("//;\n1\n2;3"), 6)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            add("//;\n1;-2;3")
        self.assertEqual(str(context.exception), "Negatives not allowed: -2")
        
        with self.assertRaises(ValueError) as context:
            add("//|\n1|2|-3|-4")
        self.assertEqual(str(context.exception), "Negatives not allowed: -3, -4")

    def test_ignore_numbers_bigger_than_1000(self):
        self.assertEqual(add("1,1000,1001"), 1001)
        self.assertEqual(add("//;\n1;1002;3"), 4)
        self.assertEqual(add("1,2000,3000,4000"), 1)
        self.assertEqual(add("1001,2000,3000,4000,5000"), 0)

    def test_custom_delimiter_of_any_length(self):
        self.assertEqual(add("//[***]\n1***2***3"), 6)
        self.assertEqual(add("//[||]\n1||2||3||4||5"), 15)
        self.assertEqual(add("//[*****]\n10*****20*****30"), 60)
        
if __name__ == "__main__":
    unittest.main()

