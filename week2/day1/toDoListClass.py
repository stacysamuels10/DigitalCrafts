#making a class
#press 1 to add task
#press 2 to delete task
# press 3 to view all tasks
# press q to puit
# while true, create class if q then false

listOfTasks = []

choice = ""

def addItem():
    itemToAdd = input("What task would you like to add?\n")
    newTask = Item(itemToAdd)
    listOfTasks.append(newTask)
    print("Your to dos:")
    for stuff in listOfTasks:
        print(stuff.name)

def removeItem():
    for stuff in listOfTasks:
        index = listOfTasks.index(stuff)
        print((index+1), stuff.name)
    itemToRemove = int(input("Please type the number of the task you would like to remove\n"))
    del listOfTasks[itemToRemove-1]
    print("Your to dos:")
    for stuff in listOfTasks:
        print(stuff.name)


class Item:
    def __init__(self, name):
        self.name = name


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
            print(stuff.name)