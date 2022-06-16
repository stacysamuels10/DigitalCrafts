import OptionsScripts
from time import sleep

whatNext = ""
openBackpack = ""
menuChoice = 0



    
# def cutSceneOne():
# print("""\nbookself, see map of library and brochure, 
#     you put both in your backpack
#     maybe they will help later
#     """)
#     sleep(2)
#     listOfMenuOptions = ["1. Look around the room", "2. Open my backpack", "3. Try the door", "4. Quit the game"]
#     print("\n")
#     for items in listOfMenuOptions:
#         print(items)
#     success = False
#     whatNext = input("\nWhat do you want to do next? Type the number to select an option\n")
#     while whatNext.isnumeric() == False:
#         print("\nPlease choose a number\n")
#         whatNext = input("\nWhat do you want to do next? Type the number to select an option\n")
#     menuChoice = OptionsScripts.menuOptions(whatNext)
#     #if menuChoice == 1:
#         #something here
#     if menuChoice == 2:
#         backpackItems = ["1. Your wand", "2. Hogwarts Student Handbook",\
#      "3. Map of Library", "4. Beginner's Guide to Wand Motions"]
#         print("\n")
#         for item in backpackItems:
#             print(item)
#         openBackpack = input("\nWhat backpack item do you want?\n")
#         backpackChoice = OptionsScripts.backpack(openBackpack)
#         while openBackpack.isnumeric() == False:
#             print("\nPlease choose a number\n")
#             openBackpack = input("\nWhat backpack item do you want?\n")
#         backpackChoice = OptionsScripts.backpack(openBackpack)
#         if openBackpack != "1" or openBackpack != "2" or \
#         openBackpack != "3" or openBackpack != "4":
#             print("Please choose a number between 1 and 4")
#             openBackpack = input("\nWhat backpack item do you want?\n")
#         if openBackpack == "1" or openBackpack == "2" or \
#         openBackpack == "3" or openBackpack == "4":
#             backpackChoice = OptionsScripts.backpack(openBackpack)
#             print(backpackChoice)
#     #if menuChoice == 3:
#         #something here

def story1 ():
    success = False
    puzzle1Code = ""
    whatNext = OptionsScripts.invokeMenuOptions()
    menuChoice = OptionsScripts.menuOptions(whatNext)
    while menuChoice == 1:
        print("""
    You walk up to the locked cabinet.
    It has a number 1-9 keypad and 4 blanks
    Maybe things in your backpack can be pieced together?        
        """)
        sleep(2)
        tryTheCode = ""
        tryTheCode = input("Would you like to 1. Enter the code to sovle the puzzle or 2. View the menu? ")
        while tryTheCode != "1" and tryTheCode != "2":
            print("Please enter 1 or 2")
            tryTheCode = input("Would you like to 1. Enter the code to sovle the puzzle or 2. View the menu? ")
        if tryTheCode == "1":
            puzzle1Code = input("Enter the code: ")
            while puzzle1Code.isnumeric() == False:
                print("\nPlease choose a number\n")
                puzzle1Code = int(input("Enter the code: "))
            while puzzle1Code != "1300":
                print("That is not the code. Please try again. The spell power increases with each incorrect guess")
                # increase spell counter
        else:
            whatNext = OptionsScripts.invokeMenuOptions()
            menuChoice = OptionsScripts.menuOptions(whatNext)
    while menuChoice == 2:

    whatNext = OptionsScripts.invokeMenuOptions()
    menuChoice = OptionsScripts.menuOptions(whatNext)
    print(menuChoice)

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
    #     backpackfunction1and2
#     if menuChoice == 3:
#         #something here

#def cutSceneTwo():

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
    #     backpackfunction3
#         #something here

# def cutSceneThree():

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
    #     backpackfunction4
#     if menuChoice == 3:
#         #something here

