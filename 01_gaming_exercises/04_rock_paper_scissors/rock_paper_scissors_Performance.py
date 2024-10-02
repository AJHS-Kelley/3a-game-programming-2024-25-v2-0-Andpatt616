# Rock, Paper, Scissors by Andrew Patton, v0.3

# MODULE IMPORTS
import random, time 

# DATA STRUCTURES -- PLAYER
playerScore = 0
playerChoice = None
numDraws = 0

# DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None

# MAIN GAME LOOP
loopCount = 0
loopsReq = int(input("How many loops do you want?\nEnter an integer, no commas, and press ENTER.\n"))
# req is the universal abbreviation in computer programming for REQUEST. reqs = REQUESTS
rpsTimeStart = time.time() # returns the number of seconds since Jan. 01, 1970 @ 12:00AM
while loopCount < loopsReq:
    
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
    #print(f"CPU choice: {cpuChoice}")
        
    # let PLAYER select choice at random.
    playerChoice = random.randint(0, 2) # randomly select 0, 1, 2.
    if playerChoice == 0:
        playerChoice = "rock"
    elif playerChoice == 1:
        playerChoice = "paper"
    elif playerChoice == 2:
        playerChoice = "scissors"
    else:
        print("Unable to determine CPU choice.\nPlease restart.\n")
        exit()


    if playerChoice == "rock" and cpuChoice == "paper":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1
        # CPU WINS
    elif playerChoice == "rock" and cpuChoice == "scissors":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1
        # PLAYER WINS
    elif playerChoice == "scissors" and cpuChoice == "rock":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1
        # CPU WINS
    elif playerChoice == "scissors" and cpuChoice == "paper":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1
        # PLAYER WINS
    elif playerChoice == "paper" and cpuChoice == "rock":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1
        # PLAYER WINS
    elif playerChoice == "paper" and cpuChoice == "scissors":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1
        # CPU WINS
    elif playerChoice == "rock" and cpuChoice == "rock":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw!\n")
        numDraws += 1
        # DRAW
    elif playerChoice == "scissors" and cpuChoice == "scissors":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw!\n")
        numDraws += 1
        # DRAW
    elif playerChoice == "paper" and cpuChoice == "paper":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw!\n")
        numDraws += 1
        # DRAW
    else:
        print("Unable to determine a winner. Please restart.\n")
        exit()
    loopCount += 1 


print(f"Your Final Score: {playerScore}\nCPU Final Score: {cpuScore}\nDraws: {numDraws}\n")
if playerScore > cpuScore:
    print(f"Congratuations, You are the winner!\n")
elif cpuScore > playerScore:
    print(f"The CPU wins. Try again next time.\n")
else:
    print("Unable to determine a winner.\nPlease restart.\n")
    exit()

rpsTimeStop = time.time()
rpsTime = rpsTimeStop - rpsTimeStart
print(f"Number of Loops: {loopCount}\n")
print(f"Execution Time {rpsTime:.2F} seconds.\n")