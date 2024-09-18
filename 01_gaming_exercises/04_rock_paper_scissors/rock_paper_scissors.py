# Rock, Paper, Scissors by Andrew Patton, v0.1

# MODULE IMPORTS
import random

# DATA STRUCTURES -- PLAYER
playerScore = 0
playerName = "Test Player"
playerChoice = None

# DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None

# PLAYER NAME INPUT
playerName = input ("Please type your name and press enter.\n")
print("Hello {playerName}!\n")
isCorrect = input("Is that correct? Type yes or no and press enter.\n").lower()

# .lower() can turn ALL input into lowercase.
# .upper() can turn ALL input into uppercase.
 
if isCorrect == "yes":
    print(f"Ok {playerName}, lets's play Rock, Paper, Scissors!\n")
else:
    playerName = input ("Please type your name and press enter.\n")

# THE RULES using MULTI-LINE STRING
print(f"""
Welcome, {playerName} to the Rock, Paper, Scissors Robot!
It's Time To Play Rock, Paper, Scissors!
      
You will play against a CPU and the first one to reach 5 points wins/
You will select either Rock, Paper, or Scissors.
The CPU will also pick Rock, Paper, or Scissors but a random.

-- ROCK BEATS SCISSORS
-- SCISSORS BEATS PAPER
-- PAPER BEATS ROCK
""")




