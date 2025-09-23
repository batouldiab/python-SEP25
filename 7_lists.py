# declaration of a list
cars = ['ford', 'toyota', 'mazda']
print(cars)

# we can also pass variables to the list
x = 'ford'
y = 'toyota'
cars = [x, y]
print(cars)

# get element by index
cars = ['ford', 'toyota', 'mazda']
second_element = cars[1] # second item
sublist = cars[0:2] # first two items
last_element = cars[-1] # last element
print(second_element)

# modify element
cars[0] = 'BMW' # replaces first element with the new value
print(cars)

# add element
cars.append('honda') # adds element to the end of the list
print(cars)
cars.insert(1, 'ford') # adds element on specific index
print(cars)
cars.insert(2, 5) # adds element on specific index
print(cars)

# remove element
cars.remove(5) # removes element 5 (only first occurence)
print(cars)
cars.remove("BMW") # removes element "BMW"
print(cars)
cars.pop(1) # removes item on specific index
print(cars)
del cars[1] # not preferable
print(cars)
cars.clear() # removes all elements in list
print(cars)
del cars # removes the cars variable completely
#print(cars) # this won't work

# Get number of elements in list:
cars = ['ford', 'toyota', 'mazda', 'toyota']
length = len(cars)
print(length)

# count of element in list
c = cars.count("toyota")
print(c)

# sorting list
# cars.sort() # alphabetical order
cars.sort(reverse=True) # reversed alphabetical order
print(cars)

cars = ['ford', 'toyota', 'Mazda', 'toyota']
# cars.sort() # capital letters are always sorted before lower cases
# print(cars)
# cars.sort( key = str.lower) # neglect capitalization for sorting
# print(cars)
cars.reverse() # reverses the order of the list
print(cars)

# copying a list
lst1 = [ 1, 2 ,3]
lst2 = lst1 # they will change toegether the values
print(lst2)
lst1[0]=10
print(lst2)

lst1 = [ 5, 6, 7]
lst2 = lst1.copy() # each list will be changed without changing the other
lst1[0]=100
print(lst2)

# concatinate lists
lst1 = ['a', 'b', 'c']
lst2 = [1,2,3]
new_list = lst1+lst2
print(new_list)

# get index of item in list
i = new_list.index("b")
print(i)