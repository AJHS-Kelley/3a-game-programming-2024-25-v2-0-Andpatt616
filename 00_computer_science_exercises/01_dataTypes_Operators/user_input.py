# User Input Practice, Andrew Patton, v0v0

# input() is the built-in to get information from the KEYBOARD
# BASIC EXAMPLE
# variableName = input("please type a variable name and press enter.\n")
# print(variableName)

# input() saves ALL INPUT TO STRING DATA TYPES DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES DEFAULT!!!

# INCORRECT, CAUSES A CONCENTRACTION ERROR.
# myNumber = input("Please type an INTEGER number and press enter.\n")
# print(myNumber = 5)

# CORRECT -- USE a wrpper
myNumber = int(input("Please type an INTEGER nuber and press enter.\n"))
print(myNumber + 5)

# Wrapper Functions
# int() will convert the data to an INTEGER if possible.
newNumber = input("Please type a value and press enter.\n")
print(int(newNumber)) # can convert STRING to INTEGER.
print(float(newNumber)) # can convert STRING to FLOAT.
print(str(newNumber)) # can convert INTEGER to STRING.

# float() will convert the data to a FLOAT if possible.
newNumber = input("Please type a value and press enter.\n")
# print(int(newNumber)) <-- cannot convert FLOAT to INTEGER.
print(float(newNumber)) # can convert STRING to FLOAT.
print(str(newNumber)) # can convert FLOAT to STRING.

# str() will convert the data to a STRING if possible.
newNumber = 5
print(newNumber + newNumber) # Should print 10
print(str(newNumber + newNumber)) # Should print 55




