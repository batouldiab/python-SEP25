# Assignment 2 Solution:
"""
Enter distinct values a, b, c, and d.
We must get a list ot two items.
both items are of value True or False.
First value is True if a>b, false otherwise.
Second value is True if c<d, false otherwise.

example: a = 1, b = 2, c = 3, d = 4
output list: [False, True]
"""
# a = 1
# b = 2
# c = 3
# d = 4
# same as:
a, b, c, d = 1, 2, 3, 4

# Solution 1:
value1 = bool(a>b)
value2 = bool(c<d)
output_list = [value1, value2]
print('output1: ', output_list)

# Solution 2:
print('output2: ',[bool(a>b), bool(c<d)])

# Solution 3:
print('output3: ',[a>b, c<d])