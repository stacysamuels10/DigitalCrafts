#pour over project
#need to determine how many orders
#need to determine small (350), medium(405), or large(480) cup per person
#nomral or strong?
#amount of grinds
#amount of water for first pour/bloom
#amount of water for second pour
#amount of water for last pour

#separate lists, enumerate lists

listOfOrders = []
moreCoffee = ""
pourAmount = 0


def prepCoffeeOrder ():
    cupSize = input("What size coffee do you want? sm, med,lg\n")
    strength = input("What kind of strength do you want? normal, strong\n")
    order = {
        "size": cupSize,
        "caffiene": strength
    }
    listOfOrders.append(order)
    
def calcCoffeeGrind(listOfOrders):
    grindAmount = 0
    pourAmount = 0
    for order in listOfOrders:
        if order["size"] == 'sm':
            if order["caffiene"] == 'normal':
                grindAmount = grindAmount + 21
                pourAmount = pourAmount + 345
            if order["caffiene"] == 'strong':
                grindAmount = grindAmount + 23
                pourAmount = pourAmount + 345
        if order["size"] == 'med':
            if order["caffiene"] == 'normal':
                grindAmount = grindAmount + 28
                pourAmount = pourAmount + 450
            if order["caffiene"] == 'strong':
                grindAmount = grindAmount + 30
                pourAmount = pourAmount + 450        
        if order["size"] == 'lg':
            if order["caffiene"] == 'normal':
                grindAmount = grindAmount + 33
                pourAmount = pourAmount + 525
            if order["caffiene"] == 'strong':
                grindAmount = grindAmount + 35
                pourAmount = pourAmount + 525
    print(f"""
    You will need to grind {grindAmount} grams of coffee.
    Your first bloom pour will be {(grindAmount*2)} grams of hot water.
    Wait 45 - 60 seconds
    Your next pour will be up to {(pourAmount/2)} grams of hot water.
    Your final pour will be up to {pourAmount} grams of hot water.
    Let the water turn to delicious bean water and enjoy!
    """)

while moreCoffee.lower() != "n":
    prepCoffeeOrder()
    moreCoffee = input("Want more coffee? Y/N \n")

calcCoffeeGrind(listOfOrders)