#pour over project
#need to determine how many orders
#need to determine small (350), medium(405), or large(480) cup per person
#nomral or strong?
#amount of grinds
#amount of water for first pour/bloom
#amount of water for second pour
#amount of water for last pour

#separate lists, enumerate lists

howManyOrders = 0
sizeOfCup = 0
strengthOfCoffee = 0
orders = []



def numberOfOrder (howManyOrders, sizeOfCup, strengthOfCoffee, orders):
    howManyOrders = howManyOrders + int(input("How many cups would you like? ")) #how many cups
    for number in range(howManyOrders): #asking what size for each one
        choiceList = """
1. Small
2. Medium
3. Large
"""
        print(choiceList)
        sizeOfCup = int(input("For coffee number %d, what size coffee would you like?   \n 1, 2, or 3? \n" % (number+1)))
        choiceList = """
        1. Normal
        2. Strong
        """
        print(choiceList)
        strengthOfCoffee = int(input("What strength would you like coffee number %d? \n 1 or 2? \n" % (number+1)))
        orders.append(howManyOrders)
        orders.append(sizeOfCup)
        orders.append(strengthOfCoffee)
    return orders
    return howManyOrders
    
#[2, 1, 1, 2, 2, 2]

#need to figure out how to access list object as an integer
def coffeeCalculations (*orders):
    for number in howManyOrders:
        print(*orders(number))
            # if orders[((number+1)*2)] == 1:
            #      print("small")
            # if orders[((number+1)*2)] == 2:
            #      print("medium")
            # if orders[((number+1)*2)] == 3:
            #     print("large")

            # if orders[((number+1)*3)] == 1:
            #      print("normal")
            # if orders[((number+1)*3)] == 2:
            #      print("strong")


numberOfOrder(howManyOrders, sizeOfCup, strengthOfCoffee, orders)
coffeeCalculations (orders)