import OptionsScripts
import backpackScripts
from time import sleep

whatNext = ""
openBackpack = ""
menuChoice = 0
success = False
completedPuzzles = []


def story1 (completedPuzzles, incorrectGuess):
    puzzle1Code = ""
    menuChoice = 0
    # whatNext = OptionsScripts.invokeMenuOptions()
    # menuChoice = OptionsScripts.menuOptions(whatNext)
    while menuChoice != 0:
        if menuChoice == 1:
            incorrectGuess = OptionsScripts.puzzle1(completedPuzzles, incorrectGuess)
            whatNext = OptionsScripts.invokeMenuOptions()
            menuChoice = OptionsScripts.menuOptions(whatNext)
        if len(completedPuzzles) == 1:
            incorrectGuess = 1
        if menuChoice == 2:
            backpackScripts.backpack1and2()
            whatNext = OptionsScripts.invokeMenuOptions()
            menuChoice = OptionsScripts.menuOptions(whatNext)
        

    

# def story2 ():

# def cutSceneTwo():

# def puzzle3 ():

# def cutSceneThree():

# def puzzle4 ():
     