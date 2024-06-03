# String Calculator

This is a simple string calculator that supports various operations on numbers provided as strings. The calculator can handle different delimiters, negative numbers, and numbers larger than 1000.

## Usage

To use the calculator, call the `add` function with a string containing numbers separated by delimiters. The `add` function returns the sum of the numbers.

```python
from calculator import add

result = add("1,2,3")  # Output: 6
print(result)

result = add("//;\n1;2;3")  # Output: 6
print(result)

result = add("//[*][%]\n1*2%3")  # Output: 6
print(result)

```

- Empty strings are treated as 0.
- Supports single numbers, two numbers separated by a comma, and multiple numbers separated by a comma.
- Supports different delimiters, including custom delimiters and delimiters of any length.
- Ignores numbers larger than 1000.
- Throws an exception for negative numbers, listing all negative numbers encountered.

## Testing
To run this function in TDD, use following command
```
python -m unittest tests.test_calculator
```

For more customization and parsing refer following link: https://osherove.com/tdd-kata-1/

## License
Feel free to use and customize it according to your project's needs! Let me know if you need further assistance!
