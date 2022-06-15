def menuOptions (whatNext): #test and works    
    menuChoice = 0
    if whatNext == "1":
        menuChoice = 1
        return menuChoice
    if whatNext == "2":
        menuChoice = 2
        return menuChoice
    if whatNext =="3":
        menuChoice = 3
        return menuChoice
    if whatNext == "4":
        print("\nThank you for playing! Bye\n")


def puzzleCounter (): #tested and works, need to append
    puzzle = 0 #at the end of each puzzle
    completedPuzzles = [0,1]
    for puzzle in completedPuzzles:
        puzzle+=1

def backpack (openBackpack):
    backpackItems = ["Your wand", "Hogwarts Student Handbook",\
     "Map of Library", "Beginner's Guide to Wand Motions" "Phone", \
     "Post it Note", "UV Blacklight Flashlight"]
    if openBackpack == "1":
        backpackChoice ="""
    Your wand from Ollivander's is so cool
    You just don't know how to use it yet.
        """
        return backpackChoice
    if openBackpack == "2":
        backpackChoice = """
    1 Galleon equals 17 Sickles
    1 Galleon equals 493 Knuts
    1 Sickle equals 29 Knuts
        """
        return backpackChoice
    if openBackpack == "3":
        backpackChoice = """
    200: Religion
    300: Social Science
    400: Literature and Poetry
    600: Technology
    900: History and Geography
        """
        return backpackChoice
    if openBackpack == "4":
        backpackChoice = """
    A Beginner's Guide to Wand Motions

    This paper has pictures that show the different movements one makes with their wand to complete the different spells.
    Leviosa: Move your wand in a circle clockwise then down
    Expelliarmus: Move your wand to the side then down
    Lumos: Sharp movement up
    Nox: Sharp movement down
    Stupefy: Move your wand diagonally then to the right
        """
        return backpackChoice
    if openBackpack == "5":
        backpackChoice = """
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
    """
        return backpackChoice
    if openBackpack == "6":
        backpackChoice = """
    1. Stupefy
    2. Lumos
    3. Leviosa
"""
        return backpackChoice
    if openBackpack == "7":
        backpackChoice = """
    You see the book suddenly light up with stars next to 5 buildings

    grinGotts wizarding bank
    Ollivanders
    twilifit and Tattings
    eeYlops owl emporium
    the leAky cauldron
    """
        return backpackChoice