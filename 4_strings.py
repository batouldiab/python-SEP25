# defining strings:
name = "mahdi" # double quotations can be used
name2 = 'mahdi' # single quotations can be used

print(name2)

# to define multiple lines string:
fullName = '''batoul
diab'''
fullName2 = """batoul
diab"""
print(fullName)

# length of string
word = "hello"
l = len(word)
print(l) # prints: 5
print(len(word)) # prints: 5

print(len("hello world")) # a space is considered a char # prints: 11


# selecting character by its index. remember, indices start with 0
name = "hello"
print(name[0]) # prints: h

word = 'hello'
first_char = word[0]
print(first_char) # prints: h

# Slicing
a = "hello world"
# the character on the right is not included in the slice
# the character on the left is included in the slice
# the negative index is counted from the end of the string
print(a[2:7]) # output: hello
print(a[:8])
print(a[2:]) # output: llo world
print(a[-5:-2]) # output: wor
print(a[-1])
print(a[-5:]) # output: world

# modifying
name = "Batoul"
print(name.upper()) # prints: BATOUL
print(name.lower()) # prints: batoul

# strip string: remove spaces in the beginning or end of a string
name = " batoul diab "
name = name.strip()
print(name)

#replace characters
name = 'batboul'
print(name.replace("ba","cz")) # prints: cztboul

# split string:
txt = "hello, batoul diab"
print(txt.split(" ")) # prints: ['hello,', 'batoul', 'diab']

# concatinating
print(name + ' ' + txt)

# checking if substring is present in a string
name = "batoul diab"
print("batoul" in name) # fiye 7ot string kbir # prints: True
print("z" in name) # fiye 7ot single character # prints: False
print("B" in name) # prints: False

splittedTxt = txt.split("l") # prints: ['he','','o, batou', ' diab']
print(splittedTxt)
print('hello' in splittedTxt)

print("z" not in name) # prints: True
print("batoul" not in name) # prints: False


# application 1 on strings
name = "baToUL" 
firstLetter = name[0].upper()
rest = name[1:].lower()
name =firstLetter+rest
print(name)

# second solution
name = "baToUL" 
firstLetter = name[0]
firstLetter = firstLetter.upper()
rest = name[1:]
rest = rest.lower()
name =firstLetter + rest
print(name)

# third solution
name = "baToUL"
print(name[0].upper() + name[2:].lower())

# Format a string
age = 20
txt = " his age is " + str(age) # this is a way to get string with number variable in it

txt2 = f"his age is {age}" # {age} is replaced with variable age. don't forget the f in the beginning
print(txt2)

price = 20.12345
txt = f"price is: {price:.3f}" # this gets the number with 3 digits after the decimal point
print(txt)



txt = f"price doubled is: {price*2}" # we can make operations in the formating
print(txt)

price_dollar = 20
priceLL = f"price is {price_dollar*90000} L.L"
print(priceLL)

priceLL = 800000
price_dollar = f"price is {priceLL/90000:.2f} dollars"
print(price_dollar)


print(f"price is {1000000/90000:.2f} dollars")

# to print qoutaions in the quotaions of the string, one way is that they must not be similar 
txt = 'My name is "Batoul"' # outer quotations for string declaration are single, inner are double
# backslash makes the single quotation considered as string character not as python syntax
txt = 'It\'s "Batoul"' 
print(txt)

# \n is inserted in the strings where we want to start a new line
word1 = "hi"
word2 = "welcome"
txt = word1 + "\n" + word2
print(txt)

sentence = "hi\nbatoul"
print(sentence)

# \t is inserted in the strings where we want to add a tab (number of spaces)
paragraph = """\tthis is a 
multiline paragraph"""

print(paragraph)

name = "batOUL"
print(name.capitalize()) # this make the first letter capital (upper case) and others letters lower case.

txt = "this is a text."
print(txt.count("is")) # counts how many times the 'is' string appeared in the string
print(txt.endswith(".")) # checks if the string ends with '.' . we can replace '.' with any string value.

# check in numeric
txt = "10"
print(txt.isnumeric()) # only this will give true
txt = "a"
print(txt.isnumeric())
txt = "a10"
print(txt.isnumeric())
txt = " 2"
print(txt.isnumeric())
txt = "10a"
print(txt.isnumeric())
