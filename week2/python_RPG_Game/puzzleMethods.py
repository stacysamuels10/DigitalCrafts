import OptionsScripts
import backpackScripts
from time import sleep

whatNext = ""
openBackpack = ""
menuChoice = 0
success = False


def story1 ():
    puzzle1Code = ""
    menuChoice = 0
    whatNext = OptionsScripts.invokeMenuOptions()
    menuChoice = OptionsScripts.menuOptions(whatNext)
    while menuChoice != 0:
        if menuChoice == 1:
            OptionsScripts.puzzle1()
            whatNext = OptionsScripts.invokeMenuOptions()
            menuChoice = OptionsScripts.menuOptions(whatNext)
        if menuChoice == 2:
            backpackScripts.backpack1and2()
            whatNext = OptionsScripts.invokeMenuOptions()
            menuChoice = OptionsScripts.menuOptions(whatNext)
        if menuChoice == 3:
            return menuChoice
        if menuChoice == 4:
            return menuChoice

story1()
def story2 ():
    puzzle2Code = ""
    menuChoice = 0
    whatNext = OptionsScripts.invokeMenuOptions()
    menuChoice = OptionsScripts.menuOptions(whatNext)
    while menuChoice != 0:
        if menuChoice == 1:
            OptionsScripts.puzzle2()
            whatNext = OptionsScripts.invokeMenuOptions()
            menuChoice = OptionsScripts.menuOptions(whatNext)
        if menuChoice == 2:
            backpackScripts.backpack1and2()
            whatNext = OptionsScripts.invokeMenuOptions()
            menuChoice = OptionsScripts.menuOptions(whatNext)
        if menuChoice == 3:
            print("This is where score will go")
        if menuChoice == 4:
            print("okay bye!")
            break

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

