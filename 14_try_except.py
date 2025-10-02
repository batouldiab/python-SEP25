# print(x) # gives an error

# defining try/except
print("try 1")
try:
    print(x)
except:
    print("error occured")

# defining try/except with specific exception
print("try 2")
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Some other error occured")

# defining try/except with specific exception and else
print("try 3")
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except ZeroDivisionError:
    print("Division by zero error")
except:
    print("Some other error occured")
else:
    print("No error occured") # this block will execute if no error occurs

# defining try/except with finally
print("try 4")
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except ZeroDivisionError:
    print("Division by zero error")
except:
    print("Some other error occured")
finally:
    print("This block will always execute") # this block will execute no matter what

# nested try/except
print("try 5")
try:
    x = input("Enter a number: ")
    x = int(x) # this will raise a ValueError if input is not a number
    try:
        val = 1 / x # this will raise a ZeroDivisionError if x = 0
    except NameError:
        print("Variable x is not defined")
    except ZeroDivisionError:
        print("Division by zero error")
    except:
        print("Some other error occured")
    finally:
        print("This block will always execute")
except:
    print("Some other error occured in the outer try block")

# Raising exceptions
print("try 6")
x = input("Enter a number: ")
if not x.isdigit():
    raise ValueError("Input is not a number") # or: raise Exception("Input is not a number")

print("try 7")
x  = "hello"
if not type(x) is int:
    raise TypeError("only integers are allowed")
    


