# #count to X
# def countToInput ():
#     num1 = 1
#     num = int(input("Number to count to: "))
#     while num1 <= num:
#         print(num1)
#         num1 += 1

# countToInput()

# #count from 1 input to the next

# def countFromToInput ():
#     num1 = int(input("Number to start counting "))
#     num = int(input("Number to count to: "))
#     if num1 < num:
#         while num1 <= num:
#             print(num1)
#             num1 += 1
#     else:
#         print("Please make sure the starting number is less than the final number")
#         countFromToInput()
# countFromToInput()

# # count odd from num1 to num

# def countFromToInputOdd ():
#     num1 = int(input("Number to start counting "))
#     num = int(input("Number to count to: "))
#     if num1 < num:
#         if num1 %2 == 1:
#             while num1 <= num:
#                 print(num1)
#                 num1 += 2
#         if num1 %2 == 0:
#             num1 +=1
#             while num1 <= num:
#                 print(num1)
#                 num1 += 2
#     else:
#         print("Please make sure the starting number is less than the final number")
#         countFromToInputOdd()
# countFromToInputOdd()

# def fizzBuzz ():
#     num = 1
#     num1 = int(input("Number to count to: "))
#     while num < num1 :
#         if num %3 == 0:
#            print("fizz")
#         if num %5 == 0:
#             print("buzz")
#         if num %3 == 0 and num %5 == 0:
#             print("fizzbuzz")
#         else:
#             print(num)
#         num += 1
# fizzBuzz ()


# #talk to grandma
# talk = 'y'
# def shoutAtGrandma ():
#     talk = input("Do you want to say something to grandma? Y/N \n")
#     while talk.lower() == 'y': 
#         talkAgain = input('What do you want to say? ')
#         if talkAgain.isupper():
#             print("NO, NOT SINCE 1938")
#             talk = input("Do you want to say something to grandma? Y/N \n")
#         if talkAgain.islower():
#             print('HUH? SPEAK UP HUNNY!')
#             talk = input("Do you want to say something to grandma? Y/N \n")
#     print('BYE')
# shoutAtGrandma()

#build a rocketship game

import time
playAgain = 'y'

def reachOrbit():
    fuelAmount = int(input("How many kilograms of fuel do you want to pack? Between 2000 and 10000\n"))
    engineCount = int(input("How many engines do you want on your ship? Between 1 and 10\n"))
    speed = 0
    height = 0
    while fuelAmount > 0:
        speed = speed + (10 * engineCount)
        speed = speed - engineCount
        speed = speed - (fuelAmount/1000)
        fuelAmount = fuelAmount - (100*engineCount)
        height = height + speed
        if height < 0:
            break
        print(height)
        print(speed)
    if height == 50000 and speed == 2000:
        print("You reached orbit!\n")
        return
    else:
        print("You came crashing down! :(\n")
        return
reachOrbit()
playAgain = input("Would you like to play again? Y/N\n")
while playAgain == 'y':
    reachOrbit()
