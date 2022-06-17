from time import sleep


def puzzle1(completedPuzzles, spellStrength):
    puzzle1Code = ""
    tryTheCode = ""
    print("""
        You walk up to the locked cabinet.
        It has a number 1-9 keypad and 4 blanks
        It says Library below it.

        You see a phone and unlock it.
        You notice the following conversation.""")
    sleep(5)
    print("""
        Phone unlocked and shows a text exchange

        Shannon: Do you know where the books are that we need for the first class?

        Jill: What books?

        Shannon: I need to find them in the library before everyone else checks them out

        Jill: Okay, I am in the library now, but what books??

        Shannon: Sizzling Scales: A Collection of Daring Dragon Poetry and Magical Maps and the Art of Not Getting Lost

        Jill: That's all?

        Shannon:  Yep- Sizzling Scales and Magical Maps.

        Jill: Dragon Rhymes and maps.  Off to the shelves to find them for us. 

        Shannon: Thanks!

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
        You place the phone in your backpack
        
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
        """)
    sleep(9.5)
    print("""
        How many Knuts should you place on the other tray to balance the scales?
            """)
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
            sleep(9.5)
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
            sleep(9.5)
            return True
        print("""
        That is not the correct amount. Please try again.
        The spell power increases with each incorrect guess
        It should be a 4 digit number
        """)
        sleep(4.4)
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
    """)
    sleep(10)
    print("""
    Which 3 directions should you move the lock?
            """)
    tryTheCode3 = input("Would you like to 1. Enter the directions of arrows to solve the puzzle or 2. View the menu? ")
    if tryTheCode3 == "1":
        puzzle3Code = input("Enter the 3 directions: ")
        if puzzle3Code.lower() == "right, up, down" or puzzle3Code.lower() == "right up down":
            print(f"""
            The lock opens and the ground rumbles. 
            Getting closer! 
            You can check your current spell level by trying the door.

            You glance at your watch and 
            see you still have time until Potions starts
            Inside the desk you see a UV Flashlight.
            You stuff in your backpack and turn to notice an old book
        """)
            print("\n===========================================================\n")
            sleep(9.4)
            print("""
            You open the book and see a map of Diagon Alley. 
            There is writing scrawled in the margins.
            """)
            print("\n===========================================================\n")
            sleep(6.4)
            print("""
        “What you see in the daytime, is hidden in the night”
        “To turn on the answer you must turn out the light”
        “The map holds the key, just 5 letters hold your fate”
        “You start from top to bottom…. hurry, or you’ll be late’ 
            """)
            print("\n===========================================================\n")
            sleep(10.5)
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
    """)
    sleep(8.3)
    print("""
    What is the spell to say to unlock the door?
            """)
    tryTheCode4 = input("Would you like to 1. Enter the spell or 2. View the menu? ")
    if tryTheCode4 == "1":
        puzzle4Code = input("Enter the spell(all 5 letters together, no spaces): ")
        if puzzle4Code.lower() == "gotya":
            sleep(2)
            return True
        print("""
        That is not the correct amount. Please try again.
        The spell power increases with each incorrect guess
        It should be 5 letters.
        """)
        sleep(3.3)
        return False
