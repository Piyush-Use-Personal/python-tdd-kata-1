def add(numbers):
    if not numbers:
        return 0

    delimiter = ','
    if numbers.startswith("//"):
        end_of_delimiter = numbers.find("\n")
        delimiter_specifier = numbers[2:end_of_delimiter]

        if len(delimiter_specifier) > 2:
            delimiter = delimiter_specifier[1:-1]
        else:
            delimiter = delimiter_specifier
        numbers = numbers[end_of_delimiter:]

    num_list = numbers.replace('\n', delimiter)
    num_list = num_list.split(delimiter)
    num_list = filter_numbers(num_list)

     # Check for negative number
    negative_numbers = [num for num in num_list if num < 0]
    if negative_numbers:
        raise ValueError("Negatives not allowed: " + ", ".join(map(str, negative_numbers)))
    
    return sum(num_list)

def filter_numbers(num_list):
    return [int(num) for num in num_list if num and int(num) <= 1000]
