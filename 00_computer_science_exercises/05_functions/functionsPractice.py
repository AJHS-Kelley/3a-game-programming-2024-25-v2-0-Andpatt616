# Functions Practice, Andrew Patton, v0.0

import random

def helloWorldMulti(): # FUNCTION SIGNATURE
    """This function will output Hello, World! in a language the user choose.""" # DOCSTRING /
    # print a list of languages to the screen, at least three but no more than five.
    print("""
        Welcome to the Hello, World! Translator
        The following languages are available.
        [E]nglish
        [S]panish
        [G]erman
        """)
    # allow the user to select (input) a choice for the language.
    language = input("What language do you want?\nPlease type the first letter of the language you want.\n").lower()

    # print "Hello, World!" to the screen in that language.
    if language == "e":
        print("In English:\nHello, World!\n")
    elif language == "g":
        print("In German:\nHallo, Walt!\n")
    elif language == "s":
        print("In Spanish:\nHola, Mundo!\n")
    else:
        print("Please type in a language!")

# helloWorldMulti() # FUNCTION CALL
    
# Function to Determine Even / Odd Numbers
argument1 = random.randint(-1000, 1000)

def isEven(argument1: int) -> bool: # Requires one ARGUMENT (argument1) and RETURNS a Boolean value.
    """Determines if an integer value is even or odd."""
    if argument1 % 2 == 0: 
        return True
    else:
        return False
    
print(isEven(argument1))

# Function With Multiple Arguments
def canRideRollerCoaster(age: int, height: int) -> bool:
    if age > 10 and height > 4:
        print("You can ride\n")
        return True
    else:
        print("You cannot ride.\n")
        return False
    
canRideRollerCoaster(4, 10) # Arguments must be passed in the same order as the function signature indicates.

