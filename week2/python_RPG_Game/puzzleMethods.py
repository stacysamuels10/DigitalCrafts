import OptionsScripts
from time import sleep

whatNext = ""
backpackChoice = ""
menuChoice = 0

def puzzle1 ():
    print("""\nbookself, see map of library and brochure, 
    you put both in your backpack
    maybe they will help later
    """)
    sleep(2)
    listOfMenuOptions = ["1. Look around the room", "2. Open my backpack", "3. Try the door", "4. Quit the game"]
    print("\n")
    for items in listOfMenuOptions:
        print(items)
    success = False
    whatNext = input("\nWhat do you want to do next? Type the number to select an option\n")
    while whatNext.isnumeric() == False:
        print("\nPlease choose a number\n")
        whatNext = input("\nWhat do you want to do next? Type the number to select an option\n")
    menuChoice = OptionsScripts.menuOptions(whatNext)
    #if menuChoice == 1:
        #something here
    if menuChoice == 2:
        backpackItems = ["1. Your wand", "2. Hogwarts Student Handbook",\
     "3. Map of Library", "4. Beginner's Guide to Wand Motions"]
        print("\n")
        for item in backpackItems:
            print(item)
        openBackpack = input("\nWhat backpack item do you want?\n")
        while openBackpack.isnumeric() == False:
            print("\nPlease choose a number\n")
            openBackpack = input("\nWhat backpack item do you want?\n")
        backpackChoice = OptionsScripts.backpack(openBackpack)
        while backpackChoice != "1" or backpackChoice != "2" or \
        backpackChoice != "3" or backpackChoice != "4":
            print(backpackChoice)
    #if menuChoice == 3:
        #something here
    

puzzle1()

# def puzzle2 ():
#     listOfMenuOptions = ["1. Look around the room", "2. Open my backpack", "3. Try the door", "4. Quit the game"]
#     whatNext = ""
#     menuChoice = 0
#     print("\n")
#     for items in listOfMenuOptions:
#         print(items)
#     success = False
#     whatNext = input("\nWhat do you want to do next? Type the number to select an option\n")
#     if whatNext.isnumeric() == False:
#         print("\nPlease choose a number\n")
#     menuChoice = OptionsScripts.menuOptions(whatNext)
#     if menuChoice == 1:
#         #something here
#     if menuChoice == 2:
#         #open backpack function
#     if menuChoice == 3:
#         #something here

# def puzzle3 ():
#     listOfMenuOptions = ["1. Look around the room", "2. Open my backpack", "3. Try the door", "4. Quit the game"]
#     whatNext = ""
#     menuChoice = 0
#     print("\n")
#     for items in listOfMenuOptions:
#         print(items)
#     success = False
#     whatNext = input("\nWhat do you want to do next? Type the number to select an option\n")
#     if whatNext.isnumeric() == False:
#         print("\nPlease choose a number\n")
#     menuChoice = OptionsScripts.menuOptions(whatNext)
#     if menuChoice == 1:
#         #something here
#     if menuChoice == 2:
#         #open backpack function
#     if menuChoice == 3:
#         #something here

# def puzzle4 ():
#     listOfMenuOptions = ["1. Look around the room", "2. Open my backpack", "3. Try the door", "4. Quit the game"]
#     whatNext = ""
#     menuChoice = 0
#     print("\n")
#     for items in listOfMenuOptions:
#         print(items)
#     success = False
#     whatNext = input("\nWhat do you want to do next? Type the number to select an option\n")
#     if whatNext.isnumeric() == False:
#         print("\nPlease choose a number\n")
#     menuChoice = OptionsScripts.menuOptions(whatNext)
#     if menuChoice == 1:
#         #something here
#     if menuChoice == 2:
#         #open backpack function
#     if menuChoice == 3:
#         #something here

class EscapeRoom:
    def __init__(self, name, spellStrength, puzzleCounter):
        self.name = name
        self.spellStrength = spellStrength
        self.puzzleCounter = puzzleCounter 