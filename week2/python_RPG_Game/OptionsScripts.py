from time import sleep


def puzzle1(completedPuzzles, spellStrength):
    puzzle1Code = ""
    tryTheCode = ""
    print("""
        You walk up to the locked cabinet.
        It has a number 1-9 keypad and 4 blanks
        It says Library below it.
        Maybe things in your backpack can be pieced together?        
            """)
    sleep(4)
    tryTheCode = input("Would you like to 1. Enter the code to solve the puzzle or 2. View the menu? ")
    if tryTheCode == "1":
        puzzle1Code = input("Enter the code: ")
        if puzzle1Code == "1300":
            print("\n===========================================================\n")
            print(f"""
        Success! Cabinet cracks open and 
        you hear a soft rumble through the floor, 
        that must be the spell easing up.
        You notice a phone next to the cabinet and
        place it in your backpack too. Maybe it 
        has some info on it to help you end the spell.
        
        You can check your current spell level by trying the door
        """)
            sleep(8)
            
            return True
        print("""
        That is not the code. Please try again.
        The spell power increases with each incorrect guess
        It should be a 4 digit number\n""")
        sleep(4)
        return False

def puzzle2(completedPuzzles, spellStrength):
    puzzle2Code = ""
    tryTheCode2 = ""
    print("""
        You walk to the cabinet and open it up
        You see an intricate unbalanced scale and 
        coins come spilling out of the cabinet.
        You vaguely remember something about the weird 
        currency in your student handbook.
        The scale has 2 Galleons and 2 Sickles in a tray. 
        
        How many Knuts should you place on the other tray to balance the scales?
            """)
    sleep(9)
    tryTheCode2 = input("Would you like to 1. Enter the number of coins to solve the puzzle or 2. View the menu? ")
    if tryTheCode2 == "1":
        puzzle2Code = input("Enter the number: ")
        if puzzle2Code == "1044":
            print(f"""
            You hear the rumble again, 
            knowing the spell is loosening
            
            You can check your current spell level by trying the door

            You also hear a creak, turn around.
            You see light coming from a door 
            you didnt notice before... 
            You walk through to a study room
        """)
            print("\n===========================================================\n")
            sleep(8)
            print("""
            You explore the room but only find 
            locked doors, a light switch, and 
            a large desk with a strange lock on the drawer. 
            Atop the desk sits a post-it with 3 spells.
                1. Stupefy
                2. Lumos
                3. Leviosa
            You put the post it note in your backpack in case you need it for later
            """)
            print("\n===========================================================\n")
            sleep(8)
            return True
        print("""
        That is not the correct amount. Please try again.
        The spell power increases with each incorrect guess
        It should be a 4 digit number
        """)
        sleep(4)
        return False

def puzzle3(completedPuzzles, spellStrength):
    puzzle3Code = ""
    tryTheCode3 = ""
    print("""
        The lock on the desk has arrows in four directions
         and a picture of a hand and wand. 
         You recognize it as a directional lock
        that only moves up, down, left, and right.
        
        Maybe you have something in your backpack 
        that can hold a clue to how to open this lock?

    \n===========================================================\n
    
    Which 3 directions should you move the lock?
            """)
    sleep(9)
    tryTheCode3 = input("Would you like to 1. Enter the directions of arrows to solve the puzzle or 2. View the menu? ")
    if tryTheCode3 == "1":
        puzzle3Code = input("Enter the number: ")
        if puzzle3Code.lower() == "right, up, down" or puzzle3Code.lower() == "right up down":
            print(f"""
            The lock opens and the ground rumbles. 
            Getting closer! 
            You can check your current spell level by trying the door.

            You glance at the clock and 
            see you still have time until Potions starts
            Inside the desk you see a UV Flashlight.
            You stuff in your backpack and turn to notice an old book
        """)
            print("\n===========================================================\n")
            sleep(8)
            print("""
            You open the book and see a map of Diagon Alley. 
            There is writing scrawled in the margins.
            """)
            print("\n===========================================================\n")
            sleep(3)
            print("""
        “What you see in the daytime, is hidden in the night”
        “To turn on the answer you must turn out the light”
        “The map holds the key, just 5 letters hold your fate”
        “You start from top to bottom…. hurry, or you’ll be late’ 
            """)
            print("\n===========================================================\n")
            sleep(9)
            return True
        print("""
        That is not the correct amount. Please try again.
        The spell power increases with each incorrect guess
        It should be a 3 directional words
        """)
        sleep(7)
        return False

def puzzle4(completedPuzzles, spellStrength):
    puzzle4Code = ""
    tryTheCode4 = ""
    print("""
        You turn off the lights, but can't see anything, 
        is there something in your backpack to help you see the book?

    \n===========================================================\n
    
    What is the spell to say to unlock the door?
            """)
    tryTheCode4 = input("Would you like to 1. Enter the spell or 2. View the menu? ")
    if tryTheCode4 == "1":
        puzzle4Code = input("Enter the spell(all 5 letters together, no spaces): ")
        if puzzle4Code.lower() == "gotya":
            return True
        print("""
        That is not the correct amount. Please try again.
        The spell power increases with each incorrect guess
        It should be a 4 digit number
        """)
        return False
