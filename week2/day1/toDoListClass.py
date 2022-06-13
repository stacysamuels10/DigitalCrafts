#making a class
#press 1 to add task
#press 2 to delete task
# press 3 to view all tasks
# press q to puit
# while true, create class if q then false

listOfTasks = []
priorityOfTasks = []

choice = ""

def addItem():
    itemToAdd = input("What task would you like to add?\n")
    prioToAdd = input("What is the task priority? High, Med, or Low\n")
    newTask = Item(itemToAdd)
    newPrio = Item(prioToAdd)
    listOfTasks.append(newTask)
    priorityOfTasks.append(prioToAdd)
    print("Your to dos:")
    for stuff in listOfTasks:
        for stuff in priorityOfTasks:
            print(f"{stuff.name} - {stuff.priority}")

def removeItem():
    for stuff in listOfTasks:
        index = listOfTasks.index(stuff, priority)
        print((index+1), stuff.name, priority)
    itemToRemove = int(input("Please type the number of the task you would like to remove\n"))
    del listOfTasks[itemToRemove-1]
    del priorityOfTasks[itemToRemove-1]
    print("Your to dos:")
    for stuff in listOfTasks:
        for stuff in priorityOfTasks:
            print(f"{stuff.name} - {stuff.priority}")



class Item:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority


while choice != "q":
    choice = input("""
    Press 1 to add task
    Press 2 to delete task
    Press 3 to view all tasks
    Press q to quit
    """)
    if choice == "1":
        addItem()
    if choice == "2":
        removeItem()
    if choice == "3":
        print("Your to dos: \n")
        for stuff in listOfTasks:
            for stuff in priorityOfTasks:
                print(f"{stuff.name} - {stuff.priority}")
