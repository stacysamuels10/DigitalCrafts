#ask user what mpg their car has
#ask how far they are going
#calculate it

#100 miles/10mog = 10 gallons * cost per gallon

usersCarMPG = 0
triplength = 0
costOfGasPerGallon = 0
costOfTrip = 0


def costCalc ():
    usersCarMPG = int(input("What gas mileage does your car get?\n"))
    triplength = int(input("How many miles are you driving?\n"))
    costOfGasPerGallon = int(input("What did you pay per gallon when you filled up?\n"))
    costOfTrip = '{:.2f}'.format((triplength / usersCarMPG) * costOfGasPerGallon)
    print(costOfTrip)

costCalc()