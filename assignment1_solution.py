# Assignment 

# Part 1: String Manipulation
"""
Create 3 variables to store: 
- A person's name (string) 
- Their age (integer) 
- Their favorite fruit (string)
"""
name = 'Harry'
age = 19
fruit = 'apple'

"""
Print a message using f-string formatting like: 
   Hello, my name is John. I am 21 years old and I love apples. 
"""
print(f"Hello, my name is {name}. I am {age} years old and I love {fruit}.")

"""
Take the name, and: 
- Print it in uppercase 
- Print it in lowercase 
- Print only the first character 
- Print the last 3 characters using slicing
"""
print("name in uppercase: ", name.upper())
l = name.lower()
print("name in lowercase: ", l)
print("First character: ", name[0])
print("last three characters: ", name[-3:])

"""
- Use .capitalize() to make the name start with a capital letter and all the other letters lowercase. 
- Count how many times the letter "a" appears in the favorite fruit. 
- Split the sentence: "Python is awesome and fun" using the space character " " and print the resulting list.
"""
print("Capitalized: ", name.capitalize())
print("Count: ", fruit.count("a"))
txt = "Python is awesome and fun" 
print("Splitted: ", txt.split(" "))
print("Splitted: ", "Python is awesome and fun".split(" "))

####################################################################################
# Part 2: Arithmetic Operations

"""
Assume the person spends 450000 L.L. each day. Calculate how much they spend in a week and 
format the result as: 
   Total weekly spending is: 3150000 L.L
"""
dailySpending = 800000
weeklySpending = dailySpending * 7
print(f"Total weekly spending is: {weeklySpending} L.L ")
print(f"Total weekly spending is: {dailySpending * 7} L.L ")

"""
Calculate how much this amount is in dollars if 1 USD = 90000 L.L. 
Print it with 2 digits after the decimal point using f-strings.
"""
rate = 90000
print(f"The amount in dollar is: {weeklySpending/rate:.2f}")
print(f"The amount in dollar is: {dailySpending*7/rate:.2f}")