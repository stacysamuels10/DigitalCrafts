import OptionsScripts
import backpackScripts

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

def gameLoop ():
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
        print("staying up late in a new friends dorm, ")
        print("you realize they have played a prank on you ")
        print("and enchanted the room so you can't get out.")
        #sleep(.7)
        print("\n===========================================================\n")
        #sleep(2.7)
        print("""You have your backpack but
        the rest of the room is new and different.
        You look at your watch.You have an hour before
        your first class of Potions. """)
        #sleep(1.2)
        print("\n===========================================================\n")
        print("""
        You look around the room and
        see a bookshelf with a map of the library
        and a brochure title 'A Beginner's Guide to Wand Motions'
        You shove both things in your backpack hoping
        they might help you later.
        """)
        print("\n===========================================================\n")
        print("""
        You might want to a grab a pen and paper 
        or to open up notes on your computer to help
        you solve the puzzles!
        """)
        print("\n===========================================================\n")
    while True:
        choice = mainMenu()
        while user.completedPuzzles == 0:
            if choice == "1":
                outcomePuzzle1 = OptionsScripts.puzzle1(user.completedPuzzles, user.spellStrength)   
                if outcomePuzzle1 == True:
                    user.spellStrength -= 30
                    user.completedPuzzles += 1
                    break
                else:
                    user.spellStrength += 10
                choice = mainMenu()
            if choice == "2":
                backpackScripts.backpack1()
                choice = mainMenu()
            if choice == "3":
                print(f"""
                The door is still locked. 
                The spell is at power: {user.spellStrength}
                Continue to complete the puzzles to lower the strength""")
                choice = mainMenu()
            if choice == "4":
                print("Thank you for playing. Bye!")
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
                    user.spellStrength+=10
                choice = mainMenu()
            if choice == "2":
                backpackScripts.backpack2()
                choice = mainMenu()
            if choice == "3":
                print(f"""
                The door is still locked. 
                The spell is at power:{user.spellStrength}
                Continue to complete the puzzles to lower the strength""")
                choice = mainMenu()
            if choice == "4":
                print("Thank you for playing. Bye!")
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
                    user.spellStrength+=10
                choice = mainMenu()
            if choice == "2":
                backpackScripts.backpack3()
                choice = mainMenu()
            if choice == "3":
                print(f"""
                The door is still locked. 
                The spell is at power:{user.spellStrength}
                Continue to complete the puzzles to lower the strength""")
                choice = mainMenu()
            if choice == "4":
                print("Thank you for playing. Bye!")
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
                    user.spellStrength+=10
                choice = mainMenu()
            if choice == "2":
                backpackScripts.backpack4()
                choice = mainMenu()
            if choice == "3":
                print(f"""
                The door is still locked. 
                The spell is at power:{user.spellStrength}
                Continue to complete the puzzles to lower the strength""")
                choice = mainMenu()
            if choice == "4":
                print("Thank you for playing. Bye!")
                break
            break
        break

gameLoop()
if user.spellStrength <= 0:
    print("""
    The ground below you rumbles a final time 
    and you switch the light back on to see the door open. 
    You grab your backpack and run out to get to Potions just in time!

    Congratulations!
    """)
else:
    print("""
    You had too many guesses and the spell strength is too high. 
    You could not get out, and Ms. McGonagall had to come and get you. 
    You missed your first day of Potions. 
    Better luck next time. """)


playAgain = ""
playAgain = input("want to play again? Y/N")
while True:
    if playAgain.lower() == "y":
        gameLoop()
    if playAgain.lower() == "n":
        print("Okay thanks for playing!")
        break