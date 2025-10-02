# For iterates through iterable objects
print('loop 1:')
fruits = ['apple', 'banana', 'cherry', 'watermelon']
for f in fruits:
    print(f)

print('loop 2:')
txt = 'any string'
for s in txt:
    if (s == ' '): # to skip space character
        continue
    print('charater is:',s)

# Break
fruits = ['apple', 'banana', 'cherry', 'watermelon']
print('loop 3:')
for f in fruits:
    print(f)
    if (f == 'banana'):
        break

print('out of for')

# Continue
fruits = ['apple', 'banana', 'cherry', 'watermelon']
print('loop 4:')
for f in fruits:
    if (f == 'banana'):
        continue
    print(f)

print('out of for')

#the range() function
"""
example:
range(6)
returns sequence of numbers,
starting by 0 (by default),
increments by 1 (by default),
ends at the specified number (6 is not included)
=> [0, 1, 2, 3, 4, 5]
"""
print('loop 5:')
for x in range(6):
    print(x)

print('loop 6: ')
for x in range(2,6): # starts by 2 instead of 0
    print(x)

print('loop 7: ')
for x in range(2,20, 3): # starts by 2 instead of 0
    print(x)

# Else statement
print('loop 8:')
for x in range(2,6): # starts by 2 instead of 0
    print(x)
else:
    print('for is done') # printable since out of for due to condition

print('loop 9:')
for x in range(2,6): # starts by 2 instead of 0
    if x == 4:
        break
    print(x)
else:
    print('for is done') # not executed since it's out of for by a break

# pass
print('loop 10:')
for i in range(5, 230, 7):
    pass
print(i)
print('out of for')

# Nested for
print('loop 11:')
adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']
for a in adj:
    for f in fruits:
        print(a, f)

# Exercise 1
"""
Using for loop, read a list from user (take 10 int inputs).
"""
print('Exercise 1:')
nums = []
for i in range(10):
    val = int(input("Enter a numeric value: "))
    nums.append(val)
print("Result:", nums)

# exercise:
"""
take 10 grades as input from user.
while taking the grades, if any grade is less than 50, the
program must stop taking inputs and write:
"Failing grade exists!"
if all grades were more than 50,
the output must be:
"The student passed all courses"
"""
print('Exercise 2:')
for i in range(10):
    inp = input(f"Enter grade {i+1}: ")
    if int(inp) < 50:
        print("Failing grade exists!")
        break
else:
    print("The student passed all courses") 