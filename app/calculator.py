def filter_numbers(num_list): #separate function so that we can add more filters going forward
    return [int(num) for num in num_list if num and int(num) <= 1000]

def add(numbers):
    if not numbers:
        return 0

    delimiter = ',' # custom delimiter
    if numbers.startswith("//"):
        delimiter_index = numbers.find("\n")
        delimiter = numbers[2:delimiter_index]
        numbers = numbers[delimiter_index + 1:]

    num_list = numbers.replace('\n', delimiter).split(delimiter)
    num_list = filter_numbers(num_list)

    # Check for negative number
    negative_numbers = [num for num in num_list if num < 0]
    if negative_numbers:
        raise ValueError("Negatives not allowed: " + ", ".join(map(str, negative_numbers)))
    
    return sum(num_list)
