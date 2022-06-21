import OptionsScripts
import backpackScripts
from time import sleep
import random

class EscapeRoom:
    def __init__(self, name, spellStrength, completedPuzzles):
        self.name = name
        self.spellStrength = spellStrength
        self.completedPuzzles = completedPuzzles



def mainMenu ():
    print("""
    1. Look around the room
    2. Open my backpack
    3. Try the door
    4. Quit the game
    """)
    choice = input("What would you like to do? Please enter a number. \n")
    return choice

user = EscapeRoom("", 100, 0)

def introLetter(): #tested and works
    name = input("""
    Hello wizard! Please enter your name!
    \n""")
    sleep(1)
    print("\n")
    print(f"""
    Welcome to Hogwarts School of Witchcraft 
    and Wizardry {name}, it is time for you 
    to be sorted into your house\n""")
    sleep(4)
    hogwartsHouses = ["Gryffindor", "HufflePuff", "Ravenclaw", "Slytherin"]
    userHouse = random.choice(hogwartsHouses)
    user.name = name + " of House " + userHouse
    print(f"You have been sorted into....\n")
    sleep(2.8)
    print(f"{userHouse}!!")
    sleep(2.2)
    print("\n")
    print(f"Henceforth, you will be known as {user.name}")
    print("\n===========================================================\n")
    sleep(3.2)
def introToGame(): #tested and works
    print(f"\n{user.name}, you've accepted your invitation to Hogwarts and finally attend as a student.")
    print("\n===========================================================\n")
    sleep(5)
    print("""
    It's your first week and after
    staying overnight in a new friends dorm,
    you wake up and realize they have played a prank on you
    and enchanted the room so you can't get out.""")
    print("\n===========================================================\n")
    sleep(9)
    print("""
    You have your backpack but
    the rest of the room is new and different.
    You look at your watch. You have an hour before
    your first class of Potions. """)
    print("\n===========================================================\n")
    sleep(9)
    print("""
    You look around the room and
    see a bookshelf with a map of the library
    and a brochure titled 'A Beginner's Guide to Wand Motions'
    You shove both things in your backpack hoping
    they might help you later.
    """)
    print("\n===========================================================\n")
    sleep(10.4)
    print("""
    You might want to a grab a pen and paper 
    or to open up notes on your computer to help
    you solve the puzzles!

    It will help if you maximize your terminal
    to be able to view puzzles and clues at the same time
    """)
    print("\n===========================================================\n")
    sleep(7)
def gameLoop ():
    #introLetter()
    #introToGame()
    while True:
        choice = mainMenu()
        while user.completedPuzzles == 0:
            if choice == "1":
                outcomePuzzle1 = OptionsScripts.puzzle1(user.completedPuzzles, user.spellStrength)   
                if outcomePuzzle1 == True:
                    user.spellStrength -= 30
                    user.completedPuzzles += 1
                    break
                if outcomePuzzle1 != True:
                    user.spellStrength += 1
            if choice == "2":
                backpackScripts.backpack1()
            if choice == "3":
                print(f"""
                The door is still locked. 
                The spell is at power: {user.spellStrength}
                Continue to complete the puzzles to lower the strength""")
                sleep(5)
            if choice == "4":
                user.completedPuzzles = 4
                break
            choice = mainMenu()
        while user.completedPuzzles == 1:
            if choice == "1":  
                outcomePuzzle2 = OptionsScripts.puzzle2(user.completedPuzzles, user.spellStrength)   
                if outcomePuzzle2 == True:
                    user.spellStrength -= 30
                    user.completedPuzzles += 1
                    break
                else:
                    user.spellStrength+=1
            if choice == "2":
                backpackScripts.backpack2()
            if choice == "3":
                print(f"""
                The door is still locked. 
                The spell is at power:{user.spellStrength}
                Continue to complete the puzzles to lower the strength""")
                sleep(5)
            if choice == "4":
                user.completedPuzzles = 4
                break
            choice = mainMenu()
        while user.completedPuzzles == 2:
            if choice == "1":  
                outcomePuzzle3 = OptionsScripts.puzzle3(user.completedPuzzles, user.spellStrength)   
                if outcomePuzzle3 == True:
                    user.spellStrength -= 30
                    user.completedPuzzles += 1
                    break
                else:
                    user.spellStrength+=1
            if choice == "2":
                backpackScripts.backpack3()
            if choice == "3":
                print(f"""
                The door is still locked. 
                The spell is at power:{user.spellStrength}
                Continue to complete the puzzles to lower the strength""")
                sleep(5)
            if choice == "4":
                user.completedPuzzles = 4
                break
# WINNER CASE -- modify to number of puzzles you want
            choice = mainMenu()
        while user.completedPuzzles == 3:
            if choice == "1":  
                outcomePuzzle4 = OptionsScripts.puzzle4(user.completedPuzzles, user.spellStrength)   
                if outcomePuzzle4 == True:
                    user.spellStrength -= 30
                    user.completedPuzzles += 1
                    break
                else:
                    user.spellStrength+=1
            if choice == "2":
                backpackScripts.backpack4()
            if choice == "3":
                print(f"""
                The door is still locked. 
                The spell is at power:{user.spellStrength}
                Continue to complete the puzzles to lower the strength""")
                sleep(5)
            if choice == "4":
                user.completedPuzzles = 4
            choice = mainMenu()
        if user.completedPuzzles == 4:
            break


gameLoop()
# playAgain = "y"
# while True:
#     if playAgain.lower() == "y":
#         gameLoop()
#         if user.spellStrength <= 0:
#             print("""
#             The ground below you rumbles a final time 
#             and you switch the light back on to see the door open. 
#             You grab your backpack and run out to get to Potions just in time!

#             Congratulations!
#             """)
#         else:
#             print("""
#             The spell strength is too high. 
#             You could not get out, and Ms. McGonagall had to come and get you. 
#             You missed your first day of Potions. 
#             Better luck next time. """)
#         playAgain = input("want to play again? Y/N")
#     if playAgain.lower() == "n":
#         print("Okay thanks for playing!")
#         break