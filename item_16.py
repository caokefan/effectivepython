# consider using a generator to override a function that returns a list directly
address = 'Four score and seven yesrs ago...'
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