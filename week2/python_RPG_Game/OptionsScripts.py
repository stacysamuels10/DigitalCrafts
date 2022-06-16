def menuOptions (whatNext): #test and works    
    menuChoice = 0
    if whatNext == "1":
        menuChoice = 1
        return menuChoice
    if whatNext == "2":
        menuChoice = 2
        return menuChoice
    if whatNext == "3":
        menuChoice = 3
        return menuChoice
    if whatNext == "4":
        print("\nThank you for playing! Bye\n")

def invokeMenuOptions ():
    listOfMenuOptions = ["1. Look around the room", "2. Open my backpack", "3. Try the door", "4. Quit the game"]
    print("\n")
    for items in listOfMenuOptions:
        print(items)
    whatNext = input("\nWhat do you want to do next? Type the number to select an option\n")
    while whatNext.isnumeric() == False:
        print("\nPlease choose a number\n")
        for items in listOfMenuOptions:
            print(items)
        whatNext = input("\nWhat do you want to do next? Type the number to select an option\n")
    return whatNext

def puzzleCounter (): #tested and works, need to append
    puzzle = 0 #at the end of each puzzle
    completedPuzzles = [0,1]
    for puzzle in completedPuzzles:
        puzzle+=1


def puzzle1():
    success = False
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
                if puzzle1Code == "1300"
                    print("""Success! Cabinet cracks open and 
                    you hear a soft rumble through the floor, 
                    that must be the spell easing up
                    """)
                    success = True
                    return success
")
                while puzzle1Code.isnumeric() == False:
                    print("\nPlease choose a number\n")
                    puzzle1Code = input("Enter the code: ")
                while puzzle1Code != "1300":
                    print("That is not the code. Please try again. The spell power increases with each incorrect guess")
                    # increase spell counter

