import random
from time import sleep
import backpackScripts
import puzzleMethods
import OptionsScripts

def introLetter(): #tested and works
    name = input("Hello wizard! Please enter your name!\n")
    sleep(1)
    print(f"""Welcome to Hogwarts School of Witchcraft 
    and Wizardry {name}, it is time for you 
    to be sorted into your house""")
    sleep(2)
    hogwartsHouses = ["Gryffindor", "HufflePull", "Ravenclaw", "Slytherin"]
    userHouse = random.choice(hogwartsHouses)
    name = name + " of House " + userHouse
    print(f"You have been sorted into....")
    sleep(1.7)
    print(f"{userHouse}!!")
    sleep(.7)
    print(f"Hence forward you will be known as {name}")

def introToGame(): #tested and works
    print("\nYou’ve accepted your invitation to Hogwarts and finally attend as a student.")
    print("\n===========================================================\n")
    sleep(2.4)
    print("It's your first week and after ")
    sleep(1.2)
    print("staying up late in a new friends dorm, ")
    sleep(1.2)
    print("you realize they have played a prank on you ")
    sleep(1.2)
    print("and enchanted the room so you can't get out.")
    sleep(.7)
    print("\n===========================================================\n")
    sleep(2.7)
    print("You have your backpack but ")
    sleep(1.2)
    print("the rest of the room is new and different. ")
    sleep(1.2)
    print("You look at your watch. ")
    sleep(1.2)
    print("You have an hour before your first class of Potions. ")
    sleep(1.2)
    print("\n===========================================================\n")

success = False

puzzleCounter = 0
spellStrength = 100
        
def puzzleCounter (completedPuzzles):
    PuzzleFinished = 0
    for puzzle in completedPuzzles:
        puzzleCounter += 1
    return puzzleCounter
def spellDecrease ():
    for i in range(puzzleCounter):
        spellStrength -= 30
    if spellDecrease < 0:
        success = True
        return spellStrength, success
def spellIncrease (incorrectGuess):
    for i in range(incorrectGuess):
        spellStrength += 10
        return spellStrength


class EscapeRoom:
    def __init__(self, name, spellStrength, puzzleCounter):
        self.name = name
        self.spellStrength = spellStrength
        self.puzzleCounter = puzzleCounter

while choice != menuChoice 4:
    user = EscapeRoom(name, 100, 0)
    whatNext = OptionsScripts.invokeMenuOptions()
    menuChoice = OptionsScripts.menuOptions(whatNext)