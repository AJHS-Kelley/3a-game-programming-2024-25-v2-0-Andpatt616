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