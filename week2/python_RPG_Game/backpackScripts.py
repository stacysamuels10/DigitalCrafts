from time import sleep
def backpack1 ():
    openBackpack = ""
    backpackChoice = ""
    backpackItems = ["1. Your wand", "2. Hogwarts Student Handbook",\
     "3. Map of Library", "4. Beginner's Guide to Wand Motions"]
    print("\n")
    for item in backpackItems:
        print(item)
    openBackpack = input("\nWhat backpack item do you want?\n")
    while openBackpack.isnumeric() == False:
        for item in backpackItems:
            print(item)
        print("\nPlease choose a number\n")
        openBackpack = input("\nWhat backpack item do you want?\n")
    while openBackpack != "1" and openBackpack != "2" \
    and openBackpack != "3" and openBackpack != "4":
        print("Please choose a number between 1 and 4")
        openBackpack = input("\nWhat backpack item do you want?\n")
    if openBackpack == "1" or openBackpack == "2" or \
    openBackpack == "3" or openBackpack == "4":
        if openBackpack == "1":
            print("""
        Your wand from Ollivander's is so cool
        You just don't know how to use it yet.
            """)
            sleep(3)
        if openBackpack == "2":
            print("""
        Student Handbook reads:
        1 Galleon equals 17 Sickles
        1 Galleon equals 493 Knuts
        1 Sickle equals 29 Knuts
            """)
            sleep(5)
        if openBackpack == "3":
            print("""
        Sections of Library:
        200: Religion
        300: Social Science
        400: Literature and Poetry
        600: Technology
        900: History and Geography
            """)
            sleep(5)
        if openBackpack == "4":
            print("""
        A Beginner's Guide to Wand Motions

        This paper has pictures that show the different movements one makes with their wand to complete the different spells.
        Leviosa: Move your wand in a circle clockwise then down
        Expelliarmus: Move your wand to the side then down
        Lumos: Sharp movement up
        Nox: Sharp movement down
        Stupefy: Move your wand diagonally then to the right
            """)
            sleep(8)
        if openBackpack == "5":
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
        """)
            sleep(10)
        if openBackpack == "6":
            print("""
        1. Stupefy
        2. Lumos
        3. Leviosa
    """)
            sleep(3)
        if openBackpack == "7":
            print("""
        You see the book suddenly light up with stars next to 5 buildings

        grinGotts wizarding bank
        Ollivanders
        twilifit and Tattings
        eeYlops owl emporium
        the leAky cauldron
        """)
            sleep(7)
def backpack2 ():
    openBackpack = ""
    backpackChoice = ""
    backpackItems = ["1. Your wand", "2. Hogwarts Student Handbook",\
     "3. Map of Library", "4. Beginner's Guide to Wand Motions", "5. Phone"]
    print("\n")
    for item in backpackItems:
        print(item)
    openBackpack = input("\nWhat backpack item do you want?\n")
    while openBackpack.isnumeric() == False:
        for item in backpackItems:
            print(item)
        print("\nPlease choose a number\n")
        openBackpack = input("\nWhat backpack item do you want?\n")
    while openBackpack != "1" and openBackpack != "2" \
    and openBackpack != "3" and openBackpack != "4" and openBackpack != "5":
        print("Please choose a number between 1 and 5")
        openBackpack = input("\nWhat backpack item do you want?\n")
    if openBackpack == "1" or openBackpack == "2" or \
    openBackpack == "3" or openBackpack == "4" or openBackpack == "5":
        if openBackpack == "1":
            print("""
        Your wand from Ollivander's is so cool
        You just don't know how to use it yet.
            """)
            sleep(3)
        if openBackpack == "2":
            print("""
        Student Handbook reads:
        1 Galleon equals 17 Sickles
        1 Galleon equals 493 Knuts
        1 Sickle equals 29 Knuts
            """)
            sleep(5)
        if openBackpack == "3":
            print("""
        Sections of Library:
        200: Religion
        300: Social Science
        400: Literature and Poetry
        600: Technology
        900: History and Geography
            """)
            sleep(5)
        if openBackpack == "4":
            print("""
        A Beginner's Guide to Wand Motions

        This paper has pictures that show the different movements one makes with their wand to complete the different spells.
        Leviosa: Move your wand in a circle clockwise then down
        Expelliarmus: Move your wand to the side then down
        Lumos: Sharp movement up
        Nox: Sharp movement down
        Stupefy: Move your wand diagonally then to the right
            """)
            sleep(8)
        if openBackpack == "5":
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
        """)
            sleep(10)
        if openBackpack == "6":
            print("""
        1. Stupefy
        2. Lumos
        3. Leviosa
        """)
            sleep(3)
        if openBackpack == "7":
            print("""
        You see the book suddenly light up with stars next to 5 buildings

        grinGotts wizarding bank
        Ollivanders
        twilifit and Tattings
        eeYlops owl emporium
        the leAky cauldron
        """)
            sleep(7)
def backpack3 ():
    openBackpack = ""
    backpackChoice = ""
    backpackItems = ["1. Your wand", "2. Hogwarts Student Handbook",\
    "3. Map of Library", "4. Beginner's Guide to Wand Motions", \
    "5. Phone", "6. Post-It Note"]
    print("\n")
    for item in backpackItems:
        print(item)
    openBackpack = input("\nWhat backpack item do you want?\n")
    while openBackpack.isnumeric() == False:
        for item in backpackItems:
            print(item)
        print("\nPlease choose a number\n")
        openBackpack = input("\nWhat backpack item do you want?\n")
    while openBackpack != "1" and openBackpack != "2" \
    and openBackpack != "3" and openBackpack != "4" and openBackpack != "5" and openBackpack != "6":
        print("Please choose a number between 1 and 6")
        openBackpack = input("\nWhat backpack item do you want?\n")
    if openBackpack == "1" or openBackpack == "2" or \
    openBackpack == "3" or openBackpack == "4" or openBackpack == "5" or openBackpack == "6":
        if openBackpack == "1":
            print("""
        Your wand from Ollivander's is so cool
        You just don't know how to use it yet.
            """)
            sleep(3)
        if openBackpack == "2":
            print("""
        Student Handbook reads:
        1 Galleon equals 17 Sickles
        1 Galleon equals 493 Knuts
        1 Sickle equals 29 Knuts
            """)
            sleep(5)
        if openBackpack == "3":
            print("""
        Sections of Library:
        200: Religion
        300: Social Science
        400: Literature and Poetry
        600: Technology
        900: History and Geography
            """)
            sleep(5)
        if openBackpack == "4":
            print("""
        A Beginner's Guide to Wand Motions

        This paper has pictures that show the different movements one makes with their wand to complete the different spells.
        Leviosa: Move your wand in a circle clockwise then down
        Expelliarmus: Move your wand to the side then down
        Lumos: Sharp movement up
        Nox: Sharp movement down
        Stupefy: Move your wand diagonally then to the right
            """)
            sleep(8)
        if openBackpack == "5":
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
        """)
            sleep(10)
        if openBackpack == "6":
            print("""
        1. Stupefy
        2. Lumos
        3. Leviosa
    """)
            sleep(3)
        if openBackpack == "7":
            print("""
        You see the book suddenly light up with stars next to 5 buildings

        grinGotts wizarding bank
        Ollivanders
        twilifit and Tattings
        eeYlops owl emporium
        the leAky cauldron
        """)
            sleep(7)
def backpack4 ():
    openBackpack = ""
    backpackChoice = ""
    backpackItems = ["1. Your wand", "2. Hogwarts Student Handbook",\
     "3. Map of Library", "4. Beginner's Guide to Wand Motions", \
     "5. Phone", "6. Post-It Note", "7. UV Blacklight Flashlight"]
    print("\n")
    for item in backpackItems:
        print(item)
    openBackpack = input("\nWhat backpack item do you want?\n")
    while openBackpack.isnumeric() == False:
        for item in backpackItems:
            print(item)
        print("\nPlease choose a number\n")
        openBackpack = input("\nWhat backpack item do you want?\n")
    while openBackpack != "1" and openBackpack != "2" \
    and openBackpack != "3" and openBackpack != "4" and \
    openBackpack != "5" and openBackpack != "6" and openBackpack != "7":
        print("Please choose a number between 1 and 7")
        openBackpack = input("\nWhat backpack item do you want?\n")
    if openBackpack == "1" or openBackpack == "2" or \
    openBackpack == "3" or openBackpack == "4" or openBackpack == "5"\
    or openBackpack == "6" or openBackpack == "7":
        if openBackpack == "1":
            print("""
        Your wand from Ollivander's is so cool
        You just don't know how to use it yet.
            """)
            sleep(3)
        if openBackpack == "2":
            print("""
        Student Handbook reads:
        1 Galleon equals 17 Sickles
        1 Galleon equals 493 Knuts
        1 Sickle equals 29 Knuts
            """)
            sleep(5)
        if openBackpack == "3":
            print("""
        Sections of Library:
        200: Religion
        300: Social Science
        400: Literature and Poetry
        600: Technology
        900: History and Geography
            """)
            sleep(5)
        if openBackpack == "4":
            print("""
        A Beginner's Guide to Wand Motions

        This paper has pictures that show the different movements one makes with their wand to complete the different spells.
        Leviosa: Move your wand in a circle clockwise then down
        Expelliarmus: Move your wand to the side then down
        Lumos: Sharp movement up
        Nox: Sharp movement down
        Stupefy: Move your wand diagonally then to the right
            """)
            sleep(8)
        if openBackpack == "5":
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
        """)
            sleep(10)
        if openBackpack == "6":
            print("""
        1. Stupefy
        2. Lumos
        3. Leviosa
    """)
            sleep(3)
        if openBackpack == "7":
            print("""
        You see the book suddenly light up with stars next to 5 buildings

        grinGotts wizarding bank
        Ollivanders
        twilifit and Tattings
        eeYlops owl emporium
        the leAky cauldron
        """)
            sleep(7)