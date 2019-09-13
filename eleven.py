# Traversing two iterators simultaneously with the zip()
names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]

longest_name = None
max_letters = 0
# using range()
''''
for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count
'''
# using enumerate()
'''
for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count
'''

# using zip()
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

print(longest_name)