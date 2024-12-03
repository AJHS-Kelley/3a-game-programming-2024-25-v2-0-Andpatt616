# Dragon Realm, <Andrew Patton>, v0.2
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time
import datetime

# SAVING DATA TO A FILE
# STEP 1 -- Create the file name to use.
logFileName = "dragonRealmLog.txt"
#Example:   dragonRealmLog1132AM.txt

# STEP 2 -- Create / Open the file to save the data.
saveData = open(logFileName, "a")
# FILE MODES
# "x" CREATES FILE, IF FILE EXISTS, EXIT WITH ERROR MESSAGE.
# "w" CREATES FILE, IF FILE EXISTS, ERASE AND OVERWRITE FILE CONTENTS.
# "a" CREATES FILE, IF FILE EXISTS, APPEND DATA TO THE FILE.

saveData.write("GAME STARTED" + " "+ str(datetime.datetime.now()) + "\n")
items = 0

hasSword = False
hasAxe = False

def displayIntro():

    print('You are in a land full of dangers. In front of you,')
    print('a dark forest and a swamp. In the dark forest there is')
    print('a goblin and in the swamp there is a giant troll.')
    print('Choose wisely on which place you want to go on.')

def chooseLocation():
    location = ''
    while location !='1' and location !='2':
        print('\nWhere do you want to go?')
        print('1.Forest')
        print('2.Swamp')
        location = input('Enter an number of your choice:')
        return location
    
def chooseWeapon():
    print('You see an sword and an axe on the ground.')
    print('Which one do you want to pick up? The [A]xe or the [S]word.')
    weapon = input().upper()
    if weapon == 'S':
        hasSword = True
        print('You have chosen the Sword!\nThe Sword is light and is meant for lightning fast attacks.')
        saveData.write("Player chose the Sword.\n")
    elif weapon == 'A':
        hasAxe = True
        print('You have chosen the Axe!\nThe Axe is heavy and is meant for very powerful attacks.')
        saveData.write("Player chose the Axe.\n")
    else:
        print('That is not an option.')
    return weapon

def checkArea(hasSword: bool, hasAxe: bool):
    saveData.write("Player decided to go to the Forest\n")
    if location == 1 and weapon == 'S':
        print('You have entered the Dark Forest...')
        time.sleep(2)
        print('The Trees are thick and the forest has a very ominous vibe to it.')
        time.sleep(2)
        print('You take a second to rest.')
        time.sleep(1)
        print('Suddenly, you are attacked by a Goblin with a dagger in its hand!')
        time.sleep(1)
        print('You draw your sword and fight the Goblin!')
        time.sleep(2)
        print('The Goblin is fast but you are faster.')
        time.sleep(2)
        print('You kill the Goblin with a swift strike!')
        time.sleep(2)
        print('You make it through the Forest safely and you continue on your journey.')
        saveData.write("Player made it through the Forest.\n")
    elif location == 1 and weapon == 'A':
        print('You have entered the Dark Forest...')
        time.sleep(2)
        print('The Trees are thick and the forest has a very ominous vibe to it.')
        time.sleep(2)
        print('You take a second to rest.')
        time.sleep(1)
        print('Suddenly, you are attacked by a goblin with a dagger in its hand!')
        time.sleep(1)
        print('You pull out your axe and fight the Goblin!')
        time.sleep(2)
        print('Because of how heavy your axe is the Goblin easly dodges all of your attacks.')
        time.sleep(2)
        print('The Goblin kills you!')
        time.sleep(2)
        print('You fail to make it through the Forest safely.')
        saveData.write("Player died to the Goblin.\n")
    elif location == 2 and weapon == 'S':
        saveData.write("Player decided to go to the Swamp\n")
        print('You have entered the Swamp...')
        time.sleep(2)
        print('The Swamp has many mud puddles and is very humid.')
        time.sleep(2)
        print('You take a second to rest.')
        time.sleep(1)
        print('Suddenly, you are attacked by a Giant Ogre with a massive club!')
        time.sleep(1)
        print('You draw your sword and fight the Ogre!')
        time.sleep(2)
        print("The Ogre is very big and bulky so your sword attack don't do much damage.")
        time.sleep(2)
        print("The Ogre smashes you with it's club")
        time.sleep(2)
        print('You fail to make it through the Swamp safely.')
        saveData.write("Player died to the Ogre.\n")
    elif location == 2 and weapon == 'A':
        print('You have entered the Swamp...')
        time.sleep(2)
        print('The Swamp has many mud puddles and is very humid.')
        time.sleep(2)
        print('You take a second to rest.')
        time.sleep(1)
        print('Suddenly, you are attacked by a Giant Ogre with a massive club!')
        time.sleep(1)
        print('You pull out your axe and fight the Ogre!')
        time.sleep(2)
        print("The Ogre is very bulky but your your axe is heavy and strong enough to do al lot of damage.")
        time.sleep(2)
        print("You kill the Ogre!")
        time.sleep(2)
        print('You make it through the swamp safely and continue your journey.')
        saveData.write("Player made it through the Swamp safely.\n")






    






# def checkCave(chosenCave):
#     print('You approach the cave...')
#     time.sleep(2)
#     print('It is dark and spooky...')
#     time.sleep(2)
#     print('A large dragon jumps out in front of you! He opens his jaws and...')
#     print()
#     time.sleep(2)

#     friendlyCave = random.randint(1, 2)

#     if chosenCave == str(friendlyCave):
#         print('Gives you his treasure!')

#     else:
#         print('Gobbles you down in one bite!')



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    location = chooseLocation()
    weapon = chooseWeapon()
    checkArea(weapon, location)
    print('Do you want to play again? (yes or no)')
    playAgain = input()



# CLOSE THE FILE
saveData.write("END OF GAME LOG\n")
saveData.close()





























































































































































































