import random
from time import sleep
def introLetter():
    name = input("Hello wizard! Please enter your name!\n")
    sleep(1)
    print(f"""Welcome to Hogwarts School of Witchcraft 
    and Wizardry {name}, it is time for you 
    to be sorted into your house""")
    sleep(2)
    hogwartsHouses = ["Gryffindor", "HufflePull", "Ravenclaw", "Slytherin"]
    userHouse = random.choice(hogwartsHouses)
    name = name + " of House " + userHouse
    print(f"You have been sorted into....")
    sleep(1.7)
    print(f"{userHouse}!!")
    sleep(.7)
    print(f"Hence forward you will be known as {name}")

#introLetter()

def introToGame():
    print("You’ve accepted your invitation to Hogwarts and finally attend as a student.")
    sleep(.7)
    print("""
    It's your first week and after 
    staying up late in a new friends dorm, 
    you realize they have played a prank on you 
    and enchanted the room so you can't get out.
    """)
    sleep(.7)
    print("""
    You have your backpack but 
    the rest of the room is new and different. 
    You look at your watch.
    You have an hour before your first class of Potions.
    """)
    sleep(.7)

    introToGame()