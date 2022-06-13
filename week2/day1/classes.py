class User:
    # name
    # height
    # weight
    # siblings
    # greeting
    def __init__(self, name, height, weight, siblings, greeting):
        self.name = name
        self.height = height
        self.weight = weight
        self.siblings = siblings
        self.greeting = greeting

rahmin = User("rahmin", "5.9", "22", "Joe", "hello" )
Olivia = User("Olivia", "5.8", "24", "Stacy", "hi" )
print(rahmin.name, rahmin.height, rahmin.greeting)
print(Olivia.User)