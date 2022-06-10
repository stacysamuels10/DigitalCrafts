#ask user what mpg their car has
#ask how far they are going
#calculate it

#100 miles/10mog = 10 gallons * cost per gallon

usersCarMPG = 0
triplength = 0
costOfGasPerGallon = 0
costOfTrip = 0
splitCost = ''
numberOfTravellers = 0


def costCalc ():
    usersCarMPG = int(input("What gas mileage does your car get?\n"))
    triplength = int(input("How many miles are you driving?\n"))
    costOfGasPerGallon = int(input("What did you pay per gallon when you filled up?\n"))
    costOfTrip = '{:.2f}'.format((triplength / usersCarMPG) * costOfGasPerGallon)
    splitCost = input("Are you splitting the cost of the trip? y/n  ")
    if splitCost == 'y'
        numberOfTravellers = int(input("How many people are splitting the cost?\nß"))
    print(costOfTrip)

costCalc()