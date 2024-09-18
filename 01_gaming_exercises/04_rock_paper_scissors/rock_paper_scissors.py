# Rock, Paper, Scissors by Andrew Patton, v0.1

# MODULE IMPORTS
import random

# DATA STRUCTURES -- PLAYER
playerScore = 0
playerName = "Test Player"
playerChoice = None
cpuScore = 0

# DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None

# PLAYER NAME INPUT
playerName = input ("Please type your name and press enter.\n")
print("Hello {playerName}!\n")
isCorrect = input("Is that correct? Type yes or no and press enter.\n").lower()

#.lower() can turn ALL 
if isCorrect == "yes":
    print(f"Ok {playerName}, lets's play Rock, Paper, Scissors!\n")
else:
    playerName = input ("Please type your name and press enter.\n")






