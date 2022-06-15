def menuOptions (whatNext): #test and works    
        if whatNext == "1":
            return menuChoice == 1
        if whatNext == "2":
            return menuChoice == 2
        if whatNext =="3":
            return menuChoice == 3
    if whatNext == "4":
        print("\nThank you for playing! Bye\n")


def puzzleCounter (): #tested and works, need to append
    puzzle = 0 #at the end of each puzzle
    completedPuzzles = [0,1]
    for puzzle in completedPuzzles:
        puzzle+=1
