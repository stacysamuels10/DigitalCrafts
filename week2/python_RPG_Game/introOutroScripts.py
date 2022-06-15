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

introLetter()