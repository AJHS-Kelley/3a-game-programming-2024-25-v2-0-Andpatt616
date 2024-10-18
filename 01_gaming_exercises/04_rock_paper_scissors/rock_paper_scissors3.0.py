# Rock, Paper, Scissors by Andrew Patton, v3.0

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
def playerName() -> str: # Function Signature -- name of function, (anrguments if any)
    """Gets the name from the player and returns it. """
    # The line above it is a DOCSTRING, it gives a brief example of what the function does.
    playerName = input ("Please type your name and press enter.\n")
    print(f"Hello {playerName}!\n")
    isCorrect = input("Is that correct? Type yes or no and press enter.\n").lower()
    if isCorrect == "yes":
        print(f"Ok {playerName}, lets's play Rock, Paper, Scissors!\n")
    else:
        playerName = input ("Please type your name and press enter.\n")
    return playerName 

# CALLING THE FUNCTION
playerName = playerName()

# THE RULES using MULTI-LINE STRING
def rules() -> None:
    """This function prints the rules for rock, paper, scissors. """
    print(f"""
    Welcome, {playerName} to the Rock, Paper, Scissors Robot!
    It's Time To Play Rock, Paper, Scissors!
        
    You will play against a CPU and the first one to reach 5 points wins.
    You will select either Rock, Paper, or Scissors.
    The CPU will also pick Rock, Paper, or Scissors but a random.

    -- ROCK BEATS SCISSORS
    -- SCISSORS BEATS PAPER
    -- PAPER BEATS ROCK
    """)
    # Does another part of this program need to access this information?
    # IF YES, YOU MUST HAVE A return STATEMENT
    # IF NO, A return STATEMENT IS NOT REQUIRED

def playerChoice() -> str:
    """Allows the player to choose rock, paper, scissors."""
    playerChoice = input("Please enter rock, paper, or scissors and press enter\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        playerChoice = input("Please enter rock, paper, or scissors and press enter\n").lower()
        if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
            print("You are not following directions. Please try again.\n")
            exit()
        print(f"You have chosen {playerChoice}.\n")
    else:
        print(f"You have chosen {playerChoice}.\n")
    return playerChoice


def cpuChoice() -> str:
    """Allows the CPU to choose rock, paper, scissors."""
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
    return cpuChoice

def pickWinner(playerChoice: str, cpuChoice: str) -> str: # playerChoice and cpuChoice are both ARGUMENTS, they will be string values.
    """This function uses the player choice and CPU choice to determine a winner."""
    if playerChoice == "rock" and cpuChoice == "paper":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1
        return "CPU Wins"
        # CPU WINS
    elif playerChoice == "rock" and cpuChoice == "scissors":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1
        # PLAYER WINS
        return "Player Wins"
    elif playerChoice == "rock" and cpuChoice == "rock":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw!\n")
        # DRAW
        return "Draw"
    elif playerChoice == "scissors" and cpuChoice == "rock":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1
        # CPU WINS
        return "CPU Wins"
    elif playerChoice == "scissors" and cpuChoice == "paper":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1
        # PLAYER WINS
        return "Player Wins"
    elif playerChoice == "scissors" and cpuChoice == "scissors":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw!\n")
        # DRAW
        return "Draw"
    elif playerChoice == "paper" and cpuChoice == "rock":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1
        # PLAYER WINS
        return "Player Wins"
    elif playerChoice == "paper" and cpuChoice == "paper":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw!\n")
        # DRAW
        return "Draw"
    elif playerChoice == "paper" and cpuChoice == "scissors":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1
        # CPU WINS
        return "CPU Wins"
    else:
        print("Unable to determine a winner. Please restart.\n")
        exit()
    # return statements IMMEDIATELY exit a function. 


# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:
    print(f"{playerName} you have {playerScore} points.\nThe CPU has {cpuScore} points.\n")
    
    
    # let cpu select choice at random.

    # print(f"CPU Choice: {cpuChoice}")

    # compare player choice to cpu choice



print(f"Your Final Score: {playerScore}\nCPU Final Score: {cpuScore}\n")
if playerScore > cpuScore:
    print(f"Congratuations {playerName}, You are the winner!\n")
elif cpuScore > playerScore:
    print(f"The CPU wins. Try again next time.\n")
else:
    print("Unable to determine a winner.\nPlease restart.\n")
    exit()