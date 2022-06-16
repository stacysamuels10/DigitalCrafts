from time import sleep


def puzzle1(completedPuzzles, incorrectGuesses):
    puzzle1Code = ""
    tryTheCode = ""
    #sleep(2)
    print("""
        You walk up to the locked cabinet.
        It has a number 1-9 keypad and 4 blanks
        It says Library below it.
        Maybe things in your backpack can be pieced together?        
            """)
    tryTheCode = input("Would you like to 1. Enter the code to solve the puzzle or 2. View the menu? ")
    if tryTheCode == "1":
        #while puzzle1Code != "1300":
        puzzle1Code = input("Enter the code: ")
        if puzzle1Code == "1300":
            print("""Success! Cabinet cracks open and 
        you hear a soft rumble through the floor, 
        that must be the spell easing up
        """)
            
            return True
        print("That is not the code. Please try again.\
    The spell power increases with each incorrect guess\n \
    It should be a 4 digit number")
        
        return False

# def story2 ():

# def cutSceneTwo():

# def puzzle3 ():

# def cutSceneThree():

# def puzzle4 ():
     