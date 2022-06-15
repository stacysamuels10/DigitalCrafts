import OptionsScripts

def puzzle1 ():
    success = False
    whatNext = ""
    listOfMenuOptions = OptionsScripts.listOfMenuOptions
    OptionsScripts.menuOptions()
    while whatNext != "4":
        whatNext = input("\nWhat do you want to do next? Type the number to select an option\n")
        for items in listOfMenuOptions:
            print(items)
        if whatNext.isnumeric() == False:
            print("\nPlease choose a number\n")
            # for items in listOfMenuOptions:
            #     print(items)
        if whatNext == "1":
            print("\nthis is where you will put the puzzle number method\n")
            break
        if whatNext == "2":
            print("\nthis is where you will put the backpack class\n")
            break
        if whatNext =="3":
            print("\nthis is where you will show the current spell level\n")
            break
    if whatNext == "4":
        print("\nThank you for playing! Bye\n")


puzzle1()





class EscapeRoom:
    def __init__(self, name, spellStrength, puzzleCounter):
        self.name = name
        self.spellStrength = spellStrength
        self.puzzleCounter = puzzleCounter 