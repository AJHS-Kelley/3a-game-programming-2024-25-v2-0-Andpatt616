# Awarding Extra Lives, Andrew Patton, v0.0

score = 99
lives = 3

# Allow the user to imput the score AS AN INTEGER
# If score is 10000 or less
    # Lose a Life
# If score is > 10000 but less than 100001
    # Give 1 Extra Life
# If score is > 100000
    # Give 2 Extra Lives

# Output the score and the number of lives to the screen.


if score > 100000:
    print(lives + 2)
elif score > 10000 < 100001:
    print(lives + 1)
else:
    print(lives - 1)





