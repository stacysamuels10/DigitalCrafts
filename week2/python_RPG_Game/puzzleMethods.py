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

def puzzle1 ():
    success = False
    whatNext = OptionsScripts.invokeMenuOptions()
    menuChoice = OptionsScripts.menuOptions(whatNext)
    if menuChoice == 1:
        print("""
    You walk up to the locked cabinet.
    It has a number 1-9 keypad and 4 blanks
    Maybe things in your backpack can be pieced together?        
        """)
        sleep(2)
        puzzle1Code = int(input("Enter the code: "))
        while puzzle1Code.isnumeric() == False:
            print("\nPlease choose a number\n")
            puzzle1Code = int(input("Enter the code: "))
        while puzzle1Code != 1300:
            print("That is not the code. Please try again. The spell power increases with each incorrect guess")
            # increase spell counter
    if menuChoice == 2:
        backpackItems = ["1. Your wand", "2. Hogwarts Student Handbook",\
     "3. Map of Library", "4. Beginner's Guide to Wand Motions", "5. Phone"]
        print("\n")
        for item in backpackItems:
            print(item)
        openBackpack = input("\nWhat backpack item do you want?\n")
        backpackChoice = OptionsScripts.backpack(openBackpack)
        if openBackpack == "1" or openBackpack == "2" or \
        openBackpack == "3" or openBackpack == "4" or openBackpack == "5":
            backpackChoice = OptionsScripts.backpack(openBackpack)
            print(backpackChoice)
        while openBackpack.isnumeric() == False:
            for item in backpackItems:
                print(item)
            print("\nPlease choose a number\n")
            openBackpack = input("\nWhat backpack item do you want?\n")
        backpackChoice = OptionsScripts.backpack(openBackpack)
        while openBackpack != "1" and openBackpack != "2" \
        and openBackpack != "3" and openBackpack != "4" and openBackpack != "5":
            print("Please choose a number between 1 and 5")
            openBackpack = input("\nWhat backpack item do you want?\n")
        backpackChoice = OptionsScripts.backpack(openBackpack)
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
    #     backpackItems = ["1. Your wand", "2. Hogwarts Student Handbook",\
    #  "3. Map of Library", "4. Beginner's Guide to Wand Motions", "5. Phone"]
    #     print("\n")
    #     for item in backpackItems:
    #         print(item)
    #     openBackpack = input("\nWhat backpack item do you want?\n")
    #     backpackChoice = OptionsScripts.backpack(openBackpack)
    #     while openBackpack.isnumeric() == False:
    #         print("\nPlease choose a number\n")
    #         openBackpack = input("\nWhat backpack item do you want?\n")
    #     backpackChoice = OptionsScripts.backpack(openBackpack)
    #     if openBackpack != "1" or openBackpack != "2" or \
    #     openBackpack != "3" or openBackpack != "4" or openBackpack != "5":
    #         print("Please choose a number between 1 and 5")
    #         openBackpack = input("\nWhat backpack item do you want?\n")
    #     if openBackpack == "1" or openBackpack == "2" or \
    #     openBackpack == "3" or openBackpack == "4" or openBackpack == "5":
    #         backpackChoice = OptionsScripts.backpack(openBackpack)
    #         print(backpackChoice)
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
    #     backpackItems = ["1. Your wand", "2. Hogwarts Student Handbook",\
    #  "3. Map of Library", "4. Beginner's Guide to Wand Motions", \
    #  "5. Phone", "6. Post-It Note"]
    #     print("\n")
    #     for item in backpackItems:
    #         print(item)
    #     openBackpack = input("\nWhat backpack item do you want?\n")
    #     backpackChoice = OptionsScripts.backpack(openBackpack)
    #     while openBackpack.isnumeric() == False:
    #         print("\nPlease choose a number\n")
    #         openBackpack = input("\nWhat backpack item do you want?\n")
    #     backpackChoice = OptionsScripts.backpack(openBackpack)
    #     if openBackpack != "1" or openBackpack != "2" or \
    #     openBackpack != "3" or openBackpack != "4" or openBackpack != "5" or openBackpack != "6":
    #         print("Please choose a number between 1 and 6")
    #         openBackpack = input("\nWhat backpack item do you want?\n")
    #     if openBackpack == "1" or openBackpack == "2" or \
    #     openBackpack == "3" or openBackpack == "4" or openBackpack == "5" or openBackpack == "6":
    #         backpackChoice = OptionsScripts.backpack(openBackpack)
    #         print(backpackChoice)
#     if menuChoice == 3:
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
    #     backpackItems = ["1. Your wand", "2. Hogwarts Student Handbook",\
    #  "3. Map of Library", "4. Beginner's Guide to Wand Motions", "5. Phone" \
    #  "6. Post-It Note", "7. UV Blacklight Flashlight"]
    #     print("\n")
    #     for item in backpackItems:
    #         print(item)
    #     openBackpack = input("\nWhat backpack item do you want?\n")
    #     backpackChoice = OptionsScripts.backpack(openBackpack)
    #     while openBackpack.isnumeric() == False:
    #         print("\nPlease choose a number\n")
    #         openBackpack = input("\nWhat backpack item do you want?\n")
    #     backpackChoice = OptionsScripts.backpack(openBackpack)
    #     if openBackpack != "1" or openBackpack != "2" or \
    #     openBackpack != "3" or openBackpack != "4" or \
    #     openBackpack != "5" or openBackpack != "6" or openBackpack != "7":
    #         print("Please choose a number between 1 and 7")
    #         openBackpack = input("\nWhat backpack item do you want?\n")
    #     if openBackpack == "1" or openBackpack == "2" or \
    #     openBackpack == "3" or openBackpack == "4" or openBackpack == "5"\
    #      or openBackpack == "6" or openBackpack == "6":
    #         backpackChoice = OptionsScripts.backpack(openBackpack)
    #         print(backpackChoice)
#     if menuChoice == 3:
#         #something here

