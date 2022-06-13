class User:
    # name
    # height
    # weight
    # siblings
    # greeting
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.weight = "none of your business"
        self.siblings = "Joe"
        self.greeting = "Hey guys"

rahmin = User("rahmin", "5.9" )
Olivia = User("Olivia", "5.8")
print(rahmin.name, rahmin.height)
print(Olivia.name, Olivia.height)