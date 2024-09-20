# Rock, Paper, Scissors by Andrew Patton, v0.3

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
print(f"Hello {playerName}!\n")
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

# MULTI-LINE STRINGS CAN BE USED AS BIG COMMENTS
"""
Anything in between the sets of double-quotes is just ignore.
If you need to write latge comments, it's easier to use multi-line strings than
putting an # in front of 15 different lines.
"""

# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:
    print(f"{playerName} you have {playerScore} pointa.\nThe CPU has {cpuScore} points.\n")
    playerChoice = input("Please enter rock, paper, or scissors and press enter\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        playerChoice = input("Please enter rock, paper, or scissors and press enter\n").lower()
        if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
            print("You are not following directions. Please try again.\n")
            exit()
        print(f"You have chosen {playerChoice}.\n")
    else:
        print(f"You have chosen {playerChoice}.\n")
    
    # let cpu select choice at random.
    cpuChoice = random.randint(0, 2) # randomly select 0, 1, 2.
    if cpuChoice == 0:
        cpuChoice = "rock"
    elif cpuChoice == 1:
        cpuChoice = "paper"
    elif cpuChoice == 2:
        cpuChoice = "scissors"
    else:
        print("Unable to determine CPU choice.\nPlease restart.\n")
        exit()
    # print(f"CPU choice: {cpuChoice}")

    # compare player choice to cpu choice
    if playerScore == "rock" and cpuChoice == "paper":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuChoice += 1
        # CPU WINS
    elif playerScore == "rock" and cpuChoice == "scissors":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerChoice += 1
        # PLAYER WINS
    elif playerScore == "rock" and cpuChoice == "rock":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw!\n")
        # DRAW
    elif playerScore == "scissors" and cpuChoice == "rock":
        pass
        # CPU WINS
    elif playerScore == "scissors" and cpuChoice == "paper":
        pass
        # PLAYER WINS
    elif playerScore == "scissors" and cpuChoice == "scissors":
        pass
        # DRAW
    elif playerScore == "paper" and cpuChoice == "rock":
        pass
        # PLAYER WINS
    elif playerScore == "paper" and cpuChoice == "paper":
        pass
        # DRAW
    elif playerScore == "paper" and cpuChoice == "scissors":
        pass
        # CPU WINS







    # print the results to the screen
    # award point to winner and output results.