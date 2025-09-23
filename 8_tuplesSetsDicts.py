# tuples:
myTuple = ("item1", "item2", "item3")
print(myTuple)
print(type(myTuple))

# sets:
mySet = {"item1", "item2","item3", "item3"}
print(mySet)
print(type(mySet))

# dict
myCar = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2018,
    "owners": ["b", "d"]
}
print(myCar)

# access a value using the key
m = myCar["model"] # method 1
m2 = myCar.get("model") # method 2
print(m2)

# get the keys defined in the dict
k = myCar.keys()
print(k)

# add to dict:
myCar["Color"] = "Black"
print(myCar)

# update dict
myCar["year"] = 2020
print(myCar)

# remove from dict:
myCar.pop("owners")
print(myCar)

print(myCar.values()) # get values in the dict

print(len(myCar.keys())) # number of keys