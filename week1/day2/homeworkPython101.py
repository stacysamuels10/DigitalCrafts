# Coin Flip
# Write a function that will flip a coin and print result
# should be a 50/50 chance of heads or tails

# import random
# sideOfCoin = random.randint(0,2) #making a random choice
# def flipACoin (): #creating a function
#     if sideOfCoin < 1:
#         print('You flipped a coin!')
#         print('It is heads!')
#     if sideOfCoin > 1:
#         print('You flipped a coin!')
#         print('It is tails')

# flipACoin() #calling the function


#Even Odd

num = int(input('Enter a number: '))

def evenOrOdd (num) :
    if (num % 2) == 0:
        print("It's Even!")
    else:
        print("It's Odd!")

evenOrOdd(num)