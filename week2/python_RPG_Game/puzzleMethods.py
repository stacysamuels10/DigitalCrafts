import OptionsScripts

whatNext = ""
def puzzle1 ():
    listOfMenuOptions = ["1. Look around the room", "2. Open my backpack", "3. Try the door", "4. Quit the game"]
    whatNext = ""
    choice = ""
    print("\n")
    for items in listOfMenuOptions:
        print(items)
    success = False
    whatNext = input("\nWhat do you want to do next? Type the number to select an option\n")
        if whatNext.isnumeric() == False:
            print("\nPlease choose a number\n")
    menuChoice = OptionsScripts.menuOptions(whatNext)
    if whatNext == "1":
        print("success!")

puzzle1()





class EscapeRoom:
    def __init__(self, name, spellStrength, puzzleCounter):
        self.name = name
        self.spellStrength = spellStrength
        self.puzzleCounter = puzzleCounter 