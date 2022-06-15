def menuOptions ():
    listOfMenuOptions = ["1. Look around the room", "2. Open my backpack", "3. Try the door"]
    for items in listOfMenuOptions:
        print(items)
    whatNext = input("What do you want to do next? Type the number to select an option\n")
    if whatNext.isnumeric() == False:
        print("Please choose a number") 


menuOptions()