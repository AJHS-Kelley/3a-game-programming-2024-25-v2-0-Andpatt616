# Flow Control Structures, Andrew Patton, v0.0
# Making Computer Programs Make Decisions

temperature = 158.78
color = "Blue"
height = 7
likesPineapplesOnPizza = False

# SINGLE DECISION POINT - if Statement
# if CONDITIONAL_EXPRESSION: <-- This will use a COMPARISON OPERATOR 99% of the time.
    # runThisCode IF the CONDITIONAL_EXPRESSION is True

if temperature > 100:
    print("It is hot as the sun outside.\n")

if color == "Blue":
    print("The sky is blue.\n")

# CHEAT CODE FOR IF STATEMENTS THAT USE BOOLEANS.
if likesPineapplesOnPizza:
    print("Gross")

# What if we want something different to happened?
if color == "Red": # COMMON ERROR FOR STUDENTS IS USING = instead of ==.
    print("Your shirt is the correct uniform color.\n")
else:
    print("Your shirt is not the correct uniform color\n")

if height == 7:
    print("You're tall enough to get on the ride")
else:
    print("You're are not tall enough to get on the ride")

# AMUSEMENT PARK HEIGHT CHECKER EXAMPLE
#Must be > min. height and < max. height to ride.
    
# When writing if-elif-else blocks check for the HIGHEST VALUE first when using > or >=    
if height >= 6:
    print("You're too tall to ride the Tea Cups!\n")
elif height >= 3:
    print("You're tall enough to ride the Tea Cups!\n")
else: # "oh, no, something's wrong!"
    print("Error, height not detected. Do not ride.\n")


# When writing if-elif-else blocks check for the LOWEST VALUE first when using < or <=
if height <= 3:
    print("You're not tall enough to ride the Tea Cups!\n")
elif height < 6:
    print("You're tall enough to ride the Tea Cups!\n")
else: # "oh, no, something's wrong!"
    print("Error, height not detected. Do not ride.\n")

if temperature >= 100:
    print("It's too hot outside.\n")
elif temperature >= 50:
    print("Recess is allowed.\n")
elif temperature > 0 < 50:
    print("Recess is in the gym.\n")
else:
    print("Error, temperature not detected.\n")