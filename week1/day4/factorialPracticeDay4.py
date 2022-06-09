
def factorial ():
    number = 0
    total = 1
    number = int(input("What number factorial are you calculating? "))
    for x in range(1, number+1):
        total = total * x
    print(total)

factorial()

def prime ():
    number = 0
    number = int(input("What number would you like to try? "))
    for x in range(1, number+1):
        if (number/2) % x == 0:
            print("this is not prime")
            return
        else:
            print("this is prime")
            return

prime ()