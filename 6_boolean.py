x= 5
y = 10

print(bool(x+2>y-1))

# false conditions (all other conditions return true):
"""
0
False
None
""
[]
{}
()
5>10
1<0
1==2
1!=1
"""

# examples:
x = 5
y = 10
print(bool(x)) # prints: True
print(bool(x>y)) # prints: False
print(bool(x+100>=y)) # prints: True

# application
# print false if value is even, true if odd
num = 5
r = num % 2
print(bool(r))