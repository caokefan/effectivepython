# be careful when iterating over the parameters: if the argument is an iterator , it
# can cause strange behavior and miss some values.
# python iterator protocol which describes how containers and iterators should
# interact with iter() and next() built-in functions, 'for' loops and related expressions.
# implement __iter__() as a generator to define your own container type.
# to judge whether a value is an iterator or a container, call the iter() twice
# while the result is same iterator, call next() to make the iterator go one step further.

def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result
'''
visits = [15, 35, 80]
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

it = read_visits('item_17_my_numbers.txt')

'''
print(list(it))
print(list(it))
'''

'''
percentages = normalize(it)
print(percentages)


percentages = normalize_copy(it)
print(percentages)
'''
def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result

path = 'item_17_my_numbers.txt'
percentages = normalize_func(lambda: read_visits(path))
print(percentages)

class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)

def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
normalize_defensive(visits)
visits = ReadVisits(path)
normalize_defensive(visits)

it = iter(visits)
normalize_defensive(it)