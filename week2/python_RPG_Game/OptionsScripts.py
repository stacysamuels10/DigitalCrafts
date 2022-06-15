def menuOptions (): #test and works
    listOfMenuOptions = ["1. Look around the room", "2. Open my backpack", "3. Try the door", "4. Quit the game"]
    whatNext = ""
    print("\n")
    for items in listOfMenuOptions:
        print(items)
    # while whatNext != "4":
    #     whatNext = input("\nWhat do you want to do next? Type the number to select an option\n")
    #     for items in listOfMenuOptions:
    #         print(items)
    #     if whatNext.isnumeric() == False:
    #         print("\nPlease choose a number\n")
    #         # for items in listOfMenuOptions:
    #         #     print(items)
    #     if whatNext == "1":
    #         print("\nthis is where you will put the puzzle number method\n")
    #         break
    #     if whatNext == "2":
    #         print("\nthis is where you will put the backpack class\n")
    #         break
    #     if whatNext =="3":
    #         print("\nthis is where you will show the current spell level\n")
    #         break
    # if whatNext == "4":
    #     print("\nThank you for playing! Bye\n")


def puzzleCounter (): #tested and works, need to append
    puzzle = 0 #at the end of each puzzle
    completedPuzzles = [0,1]
    for puzzle in completedPuzzles:
        puzzle+=1
