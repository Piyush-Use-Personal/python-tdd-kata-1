def add(numbers):
    if not numbers:
        return 0
    
    num_list = numbers.replace('\n', ',').split(',')
    num_list = [int(num) for num in num_list if num]
    return sum(num_list)
