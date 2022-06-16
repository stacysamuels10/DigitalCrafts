import random
from time import sleep
import backpackScripts
import puzzleMethods
import OptionsScripts
puzzleCounter = 0
# spellStrength = 100
# name = ""
success = False
# completedPuzzles = []
# incorrectGuess = 0

def introLetter(): #tested and works
    name = input("Hello wizard! Please enter your name!\n")
    #sleep(1)
    print(f"""Welcome to Hogwarts School of Witchcraft 
    and Wizardry {name}, it is time for you 
    to be sorted into your house""")
    #sleep(2)
    hogwartsHouses = ["Gryffindor", "HufflePull", "Ravenclaw", "Slytherin"]
    userHouse = random.choice(hogwartsHouses)
    name = name + " of House " + userHouse
    print(f"You have been sorted into....")
    #sleep(1.7)
    print(f"{userHouse}!!")
    #sleep(.7)
    print(f"Hence forward you will be known as {name}")
    return name

def introToGame(): #tested and works
    print("\nYou’ve accepted your invitation to Hogwarts and finally attend as a student.")
    print("\n===========================================================\n")
    #sleep(2.4)
    print("It's your first week and after ")
    #sleep(1.2)
    print("staying up late in a new friends dorm, ")
    #sleep(1.2)
    print("you realize they have played a prank on you ")
    #sleep(1.2)
    print("and enchanted the room so you can't get out.")
    #sleep(.7)
    print("\n===========================================================\n")
    #sleep(2.7)
    print("You have your backpack but ")
    #sleep(1.2)
    print("the rest of the room is new and different. ")
    #sleep(1.2)
    print("You look at your watch. ")
    #sleep(1.2)
    print("You have an hour before your first class of Potions. ")
    #sleep(1.2)
    print("\n===========================================================\n")
    #add cut scene 1




def spellStrengthChange (completedPuzzles, spellStrength, incorrectGuess):
    for i in completedPuzzles:
        user.spellStrength = user.spellStrength - 30
    # print(user.completedPuzzles, user.spellStrength, incorrectGuess)
    if spellStrength < 0:
        success = True
    for i in range(incorrectGuess):
        user.spellStrength += 10
    # print(user.spellStrength)
    # print(incorrectGuess)


class EscapeRoom:
    def __init__(self, name, spellStrength, completedPuzzles, incorrectGuesses):
        self.name = name
        self.spellStrength = spellStrength
        self.completedPuzzles = completedPuzzles
        self.incorrectGuesses = incorrectGuesses


user = EscapeRoom(name="", spellStrength=100, completedPuzzles=[], incorrectGuesses=0)

def EscapeRoom ():
    choice = puzzleMethods.menuChoice
    introLetter()
    introToGame()
    while choice !=  4 and choice != 3:
        user.incorrectGuesses = puzzleMethods.story1(user.completedPuzzles, user.incorrectGuesses)
        spellStrengthChange(user.completedPuzzles, user.spellStrength, user.incorrectGuesses)
    if choice == 3:
        print(spellStrength)
    if choice == 4:
        print("Thank you for playing. Bye!")

EscapeRoom()

#choice 3 prints out spell strength
#choice 4 exits
#option to play again
#finish out puzzles 2-4