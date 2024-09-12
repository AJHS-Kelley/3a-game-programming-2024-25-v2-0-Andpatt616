# Awarding Extra Lives, Andrew Patton, v0.0

score = int(input("Please put your score here\n"))
lives = 3
name = "Andrew"

print(F"Hello {name}! You scored {score} points.\n")

# CHARACTER REFERENCE
# CURLY BRACES {}
# BRACKETS []
# ANGLE-BRACKETS <>
# PARENTHESES ()

# Allow the user to input the score AS AN INTEGER
# If score is 10000 or less
    # Lose a Life
# If score is > 10000 but less than 100001
    # Give 1 Extra Life
# If score is > 100000
    # Give 2 Extra Lives

# Output the score and the number of lives to the screen.


if score <= 10000:
    lives -= 1
elif score < 100001:
    lives += 1
elif score > 100000:
    lives += 2


print ("lives " + str(lives))
print("score " + str(score))






