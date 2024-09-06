# Loops, Andrew Patton, v0.0

# TWO TYPES OF LOOPS
# for <-- Used when you know how many loops you'll need.
# while <-- Used when you do not know how many loops you'll need.

# for loop is like GO FISH, you search each card for what the player asked.
# while loop is like a musical chairs, you move around until the music stops.

# EACH TRIP THROUGH THE ENTIRE LOOP IS CALLED AN iteration
# "iterate through the list" means use a for loop

# for loop example -- Iterating a List
# fruits = ["apple", "banana", "strawberry", "tomato"]
# for eachFruit in fruits:
#     print(eachFruit)

# # continue Keyword -- Skips the current iteration and then finishes the loop.
#     fruits = ["apple", "banana", "strawberry", "tomato"]
# for eachFruit in fruits:
#     if eachFruit == "banana":
#         continue
#     print(eachFruit)

# break Keyword -- Immediately exit the loop.
fruits = ["apple", "banana", "strawberry", "tomato"]
for eachFruit in fruits:
    if eachFruit == "banana":
        break
    print(eachFruit)