# Dragon Realm, <Andrew Patton>, v0.1
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import time

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
    hasSword = False
    hasAxe = False
    print('You see an sword and an axe on the ground. Which one do you want to pick up? Enter 1 to pick up the sword and enter 2 to pick up the axe.')
    choice = input().lower()
    if choice == '1':
        hasSword = True
        print('You have chosen the Sword!\nThe Sword is light and is meant for lightning fast attacks.')
    elif choice == '2':
        hasAxe = True
        print('You have chosen the Axe!\nThe Axe is heavy and is meant for very powerful attacks.')
    else:
        print('That is not an option.')
    return chooseWeapon

def checkForest(hasSword):
    print('You have entered the Dark Forest...')
    time.sleep(2)
    print('The Trees are thick and the forest has a very ominous vibe to it.')
    time.sleep(2)
    print('You take a second to rest.')
    time.sleep(1)
    print('Suddenly, you are attacked by a goblin with a dagger in its hand!')
    time.sleep(1)
    if hasSword:
        print('You draw your sword and fight the Goblin!')
        time.sleep(2)
        print('The Goblin is fast but you are faster.')
        time.sleep(2)
        print('You kill the goblin with a swift strike!')
    else:
        print('you die')
    






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
    chooseWeapon()
    checkForest(location)
    print('Do you want to play again? (yes or no)')
    playAgain = input()