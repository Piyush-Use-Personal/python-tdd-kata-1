def add(numbers):
    if not numbers:
        return 0

    delimiters = [',']
    if numbers.startswith("//"):
        end_of_delimiter = numbers.find("\n")
        delimiter_specifier = numbers[2:end_of_delimiter]

        if delimiter_specifier.startswith("[") and delimiter_specifier.endswith("]"):
            delimiter_specifier = delimiter_specifier[1:-1]
            delimiters = delimiter_specifier.split("][")
        else:
            delimiters = [delimiter_specifier]
            
        numbers = numbers[end_of_delimiter + 1:]

    for delimiter in delimiters:
        numbers = numbers.replace(delimiter, ',')

    num_list = numbers.replace('\n', ',') # use specific delimiter for further process
    num_list = num_list.split(',')
    num_list = filter_numbers(num_list)

    # Check for negative numbers
    negative_numbers = [num for num in num_list if num < 0]
    if negative_numbers:
        raise ValueError("Negatives not allowed: " + ", ".join(map(str, negative_numbers)))
    
    return sum(num_list)

def filter_numbers(num_list):
    return [int(num) for num in num_list if num and int(num) <= 1000]
