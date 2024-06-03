def add(numbers):
    if not numbers:
        return 0

    delimiter = ','
    if numbers.startswith("//"):
        delimiter_index = numbers.find("\n")
        delimiter = numbers[2:delimiter_index]
        numbers = numbers[delimiter_index + 1:]

    num_list = numbers.replace('\n', delimiter).split(delimiter)
    num_list = [int(num) for num in num_list if num]
    return sum(num_list)
