# Coin Flip
# Write a function that will flip a coin and print result
# should be a 50/50 chance of heads or tails
from time import sleep
print ("\n")
print("Let's play 3 games!")
sleep(1)
print("First up: Flip a coin!")
sleep (1)

import random
sideOfCoin = random.randint(0,2) #making a random choice
def flipACoin (): #creating a function
    if sideOfCoin < 1:
        print('You flipped a coin!')
        print('\nIt is heads!')
    if sideOfCoin > 1:
        print('You flipped a coin!')
        print('\nIt is tails!')

flipACoin() #calling the function

print("\n")
sleep (1)
print("Next is your lucky number odd or even?")
sleep(1)

#Even Odd
#write a function when given a number as an input, it tells the user if it is even or odd

num = int(input('Enter your favorite number: '))

def evenOrOdd (num) :
    if (num % 2) == 0:
        print("\nIt's Even!")
    else:
        print("\nIt's Odd!")

evenOrOdd(num)

print("\n")
sleep(1)
print("Last one!\n")
sleep(1)

# dice roller
# write a function that take two numbers as arguments #int(input())
#write a script that tells the user we are rolling a dice and they need to decide number of sides
#chooses a random integer within the amount the user gave

import random

print("Let's roll a dice!")

pickADice = int(input('How many sides should it have? (2-20): '))

diceSides = random.randint(2,pickADice)

def rollTheDice (diceSides):
    print("It's rolling...\n")
    sleep(2)
    print("You rolled " + str(diceSides) + "!")

rollTheDice(diceSides)
print("\n")