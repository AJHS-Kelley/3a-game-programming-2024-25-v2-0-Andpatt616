# Data Types and Operators, Andrew Patton, v0.0

# Fundamental Data Types
# String - str - Sequence of letter, numbers, spaces, or other characters.
# Strings in Python are inside ' ' or " "
# idc if you use ' ' or " " just be consistent.

# Boolean - bool - True or False values.

# Float - float - any number with a decimal, +/-, including 0.0.

# Integers - int - any whole numbers, +/-, including 0.

# Data types are stored in VARIABLES.
# A variable is basically a bucket with a name to put data into.
# VARIABLE NAMES SHOULD TELL YOU WHAT DATA IS BEING STORED IN IT.
# VARIABLES CANNOT START WITH A NUMBER
# camelCaseVariableNames
# snake_case_variable_names

# DECLARING VARIABLES AND ASSIGNING VALUES

high_score = 83745512 # int data types
highScore = 304872612 # int data types

carSpeed = 123.2341 # float data type, miles per hour
car_speed = 5.29342 # float data type, miles per hour

hasAxe = True # boolean data type
isPurple = False # boolean data type

playerName = "Andrew Patton" # string data type
player_dialoge = "Hello there" # string data type

# ASSIGN NEW VALUES
playerName = "Paul goodman"
car_speed = 2.34

# DATA TYPES CAN CHANGE, BE CAREFUL
hasAxe = 3.67

# Printing Data Types
newInt = 3
newFloat = 4.0
newString = "Skibidi Toilet"
newBool = False

# print(type(newInt))
# print(type(newFloat))
# print(type(newString))
# print(type(newBool))

# printing Variables to Console / Screen
# print(high_score)
# print(car_speed)
# print(hasAxe)
# print(player_dialoge)

# printing variables and expressions to console / screen
# print(high_score + 5024)
# print(26 * 254)
# print(high_score)


# PRINTING VARIABLES INSIDE OF STRINGS
# print(f"Hello {playerName}. Your new high score is {highScore}.\n")

# ARITHMETIC OPERATORS
myInt = 4
myFloat = 3.75
myNum = 0

#addition
myInt = 9 + 2
myFloat = 9.75 + 2.0

myInt = myInt + 5

myNum = myInt + myFloat
# When you add an Int and a float together, the answer becomes a float

# subtraction
myNum = myInt - myFloat
myInt = myFloat - 1.25

# Multiplication
myNum = myInt * myFloat

# Division
myNumber = myInt / myFloat # first is numerator, second num is denominator

# MODULUS (MODULO) % -- Returns REMAINDER after dividing.
# MOST COMMON USE FOR MADULUS IS DETERMINING EVEN / ODD NUMBERS
numStudents = 6
numSlicesPizza = 36

leftOvers = numSlicesPizza % numStudents
# print(leftOvers)

# EXPONENTS **
numSquared = 5 ** 2 # 5 is base, 2 is the exponent.

# FLOOR-DIVISION // -- Divides, throws out any decimal.
myNum = myInt // myFloat

# Addition-Assignment Operator - Mostly used for counters.
myNum = 5
myNum = myNum + 1 # Old-School Method
myNum += 1 # New Hotness
myNum *= 1
myNum /= 1


# COMPARISON OPERATORS

# IS-EQUAL-TO == Are the two values equal to each other?
# Returnes True or False based on evaluation.
x = 12.0
# print(x == 5)

# NOT-EQUAL TO != Are the two values NOT equal?
# Return True or False based on evaluation.
# print(x != 12)

# GREATER THAN / GREATER-THAN-OR-EQUAL TO
# print(5 > 3) # Greater Than
# print(12 >= 2) # Greater Than or equal To

# LESS THAN / LESS-THAN-OR-EQUAL TO
# print(5 < 3) # LESS Than
# print(12 <= 2) # LESS Than or equal To

# LOGICAL OPERATORS
# and -- ALL CONDITIONS MUST BE TRUE FOR THE ENTIRE STATMENT TO BE TRUE.
age = 16
height= 67.2
eyeColor = "Brown"
# In order to ride the Teacups, you must be at least 18 years old and at least 60" tall
# print(age >= 18 and height >= 60)
# print(age >= 18 and height >= 60 and eyeColor == "Blue")
# ALWAYS CHECK FOR THE MOST-LIKELY TO BE FALSE CONDITION FIRST!!!!!
# print(defeatedBoss == True and level > 5 and hasBlueKey == True)


# or -- AT LEAST ONE CONDITION MUST BE TRUE FOR THE ENTIRE STATMENT TO BE TRUE
# print(age >= 18 or height >= 60)
# print(age >= 18 or height >= 60 or eyeColor == "Blue")
# ALWAYS CHECK FOR THE MOST-LIKELY TO BE TRUE CONDITION FIRST!!!!!
# print(defeatedBoss == True or level > 5 or hasBlueKey == True)

# not -- RETURNS THE OPPOSITE VALUE OF THE STATEMENT.
a = 7
# print(a == 7)
# print(not(not (a == 7)))

# COMBINING LOGICAL OPERATORS
# print(a == 7 and hasKey == True or isCloud == True)
# True and

# IDENTITY OPERATORS
g = 1.0
h = 1.0
i = g
#print(g is h)
#print(i is not 1.0)
#print(i is not g)

# MEMBERSHIP OPERATORS
fruits = ["apple", "banana", "tomato"]
#print("banana" in fruits)
#print("potato" in fruits)




