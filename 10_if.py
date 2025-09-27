# if
a = 5
b = 10
if a>b :
    print("a more than b")

# if .. else
a = 5
b = 10
if a>b :
    print("a more than b")
else:
    print("b more than a")
print("out of if")

# if ...elif .. else
a = 10
b = 10
if a>b :
    print("a more than b")
elif a<b:
    print("b more than a")
else:
    print("a and b are equal")
    
print("out of if")

# nested if (example 1)
a = 10
b = 10
if a>b :
    print("a more than b")
else:
    if b>a : 
        print("b more than a")
    else: 
        print("they are equal")
    print("something")
    
print("out of if")

# nested if (example 2)
a = 2
if a > 5:
    print("above 5")
    if a>15:
        print("and above 15")
    else:
        print("but not above 15")

# operations within if:
# to get a number between two integers:
x = 8
if x>0:
    if x<10:
        print("x is between 0 and 10.")

if x<10:
    if x>0:
        print("x is between 0 and 10.")    

if x >0 and x<10: #checks both conditions, both must be true to execute the if
    print("it is between 0 and 10.")

# check if it's less than 10, more than 0, and not equal to 5:
if x<10 and x>0 and x!=5: # we can use "and" operator as much as we need
    print("it meets all conditions")

# or operator:
a =  70
b = 40
c =30
if (a < c) or (b < c): # needs only one condition to return true for the if to be executed
    print("at least one of a or b is less than c")
else:
    print("both are more than c.")