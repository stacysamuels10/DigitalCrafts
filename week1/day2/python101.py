# #small 1, hello you
# name = input('What is your name? ')
# print("Hello, " + name + "!")

# #small 2, HELLO YOU!

# newName = input('WHAT IS YOUR NAME? ')
# lengthOfName = len(newName)

# print("HELLO, " + newName.upper() + "!")
# print("YOUR NAME HAS " + str(lengthOfName) + " LETTERS IN IT! AWESOME")


# #small 3 madlib

# print("Please fill in the blanks below:")
# print("____(name)____'s favorite subject in school is ____(subject)____.")

# madlibName = input('What is name? ')
# madlibFavSubject = input('What is subject? ')

# print(madlibName + "'s favorite subject in school is " + madlibFavSubject + ".")

# #small 9

# for i in range(5):
#     print ("*****")


# #small 10 Print a Square II

# squareSize = int(input('How big is the square? '))

# for i in range(squareSize):
#     print("*"*squareSize)

# bill = int(input('What was your bill? '))
# tip = int(input('What tip would you like to give? Put it in a percentage. '))

# moola = 0
# finalTotal = 0

# def tipCalc(moola):
#     moola = bill + (bill * tip * 0.01)
#     finalTotal = '{:.2f}'.format(moola)
#     print("This is your tip")
#     print(finalTotal)

# tipCalc(bill)

# bill1 = int(input('What was your bill? '))
# tip1 = input('Level of Service? good, fair or bad? ')

# moola1 = 0
# finalTotal1 = 0
# def tipCalc1(moola1):
#     if tip1 'good':
#         moola1 = bill1 + (bill1 * .2)
#         finalTotal1 = '{:.2f}'.format(moola1)
#     if tip1 'fair':
#         moola1 = bill1 + (bill1 * .15)
#         finalTotal = '{:.2f}'.format(moola1)
#     if tip1 'bad':
#         moola1 = bill1 + (bill1 *.1)
#         finalTotal ='{:.2f}'.format(moola1)

# tipCalc1(bill1)


#guess the number

import random
secret_number = random.randint(1,10)

print('I am thinking of a number between 1 and 10.')
print('You have 5 guesses left')
userGuess = 0
numberOfGuesses = 5

for i in range(numberOfGuesses):
    while userGuess != secret_number: #while a user is not guessing the right number
        userGuess = int(input ("Whats the number? "))
        if userGuess == secret_number:
            break
        if userGuess > secret_number:
            print(str(userGuess) + " is too high")
            print("You have " + str(numberOfGuesses) + " guesses left.")
        if userGuess < secret_number:
            print(str(userGuess) + " is too low")
            print("You have " + str(numberOfGuesses) + " guesses left.")

print("Yes! You win!") #printing if they do win



