# consider using a generator to override a function that returns a list directly
# using generator is more clear than returning result as a list to the caller
# no matter how big the input is, the generator can generate a series of outputs
# because these inputs and outputs will not affect the memory consumed during execution
from itertools import islice

address = 'Four score and seven years ago...'
'''
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index+1)
    return result

result = index_words(address)
print(result[:3])
'''

def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

result = list(index_words_iter(address))
print(result)

def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
            for letter in line:
                offset += 1
                if letter == ' ':
                    yield offset

with open('item_16_address.txt', 'r') as f:
    it = index_file(f)
    results = islice(it, 0, 3)
    print(list(results))