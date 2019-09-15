# be careful when iterating over the parameters
visits = [15, 35, 80]

def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result
'''
percentages = normalize(visits)
print(percentages)
'''

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

def normalize_copy(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

it = read_visits('my_numbers.txt')

'''
print(list(it))
print(list(it))
'''

'''
percentages = normalize(it)
print(percentages)
'''

percentages = normalize_copy(it)
print(percentages)
