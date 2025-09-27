"""
While loops definition:
A while loop is used to execute a block of code repeatedly as long as a specified condition is true.
The condition is checked before the execution of the loop body.
"""

# example
x = 6

# infinite loop
# while x == 6:
#     print("inf loop")

# false condition from the beginning
while x > 10:
    print("x greater than 10")

print("out of while loop")

# simple while loop (incrementing in the loop)
print("loop 1")
i = 1
while i < 5:
    print(i)
    i = i + 1 # don't forget to increment the variable in the loop

print("out of loop 1")

# incrementing in the loop example 2
print("loop 2")
i = 1
while i < 5:
    i = i + 1 
    print(i)

print("out of loop 2")