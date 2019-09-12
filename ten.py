# Try to replace the range() with enumerate().
# 1) enumerate() function provide a streamlined way of writing,
# the index of each element was known as traversing the iterator.
# 2) try to use enumerate() to override the traversal code
# that combines "range" with subscript access.
# 3) enumerate() can accept the second parameter which specifies
# the value at the start of counting(The default is 0).
flavor_list = ['Mathematical Analysis', 'Mathematical Statistics',
                     'Machine Learning', 'Statistical Learning']

# range
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('%d: %s' % (i + 1, flavor))

# enumerate
for i, flavor in enumerate(flavor_list):
    print('%d: %s' % (i + 1, flavor))

'''
for i, flavor in enumerate(flavor_list, 1):
    print('%d: %s' % (i + 1, flavor))
'''