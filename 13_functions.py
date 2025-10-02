# defining a function
print("function example 1:")
def myFunc():
    print("hi from the function")

myFunc()

# pass arguments:
print("function example 2:")
def myFunc(fname):
    print("Hello", fname)
myFunc("Batoul")

# passing multiple arguments:
print("function example 3:")
def myFunc(fname, lname):
    print("Hello", fname, lname)
myFunc("Batoul", "Diab")

# Arguments order:
print("function example 4:")
def myFunc(child1, child2, child3):
    print("Youngest child is "+ child3)
myFunc(child1="AAA", child3="BBB", child2="CCC")

#exercise:
"""
take two input numbers & pass to function to calculate and print: 
their sum, subtraction, multiplication, and division
"""
print("function example 5:")
def myFunc(input1, input2):
    print("The sum is: ", input1+input2)
    print("The subtraction (absolute) is: ", abs(input1-input2))
    print("The multiplication is: ", input1*input2)
    if(int(input2) != 0):
        print(f"The division is: {int(input1) / int(input2)}")
    else:
        print("Division can't be performed.")
        
v1 = int(input("value 1: "))
v2 = int(input("value 2: "))
myFunc(int(v1),int(v2))

# function with default parameters
print("function example 6:")
def func(country= "Lebanon"):
    print("the country is: "+country)
func("USA")
func()

## func with list:
# normal passed variable changed in function
print("function example 7:")
def func(v):
    v=v+2
    print(v)

val = 3
func(val)
print(val)

# list passed as argument and changed in function
print("function example 8:")
def func(lst):
    lst[1]='z'
    print(lst[1])

l = ['a','b','c']
func(l)
print(l)
"""
unlike other variables, any modification applied to the list 
in the function will cause the modification of the original list.
""" 

# returning values:
print("function example 9:")
def myFunc(v):
    res = v * 2
    return res # the function will return the value of res

r = myFunc(5) # r will get the value of res
print(r)
r2 = myFunc(7)
print(r2)


# recursion:
def myFunc(n):
    if n > 0:
        print(n)
        myFunc(n-1)
    else:
        print("done")

myFunc(5)
# the function will call itself until n=0
# the function will print 5,4,3,2,1,0
# then print "done"

# example 2:
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


# for empty function
def test():
    pass