#class example

class Room:
    #dimensions
    #window
    #doors
    #flooring
    #name/type of room
    #contents
    def __init__(self, dimensions, windows, doors, flooring, name, contents): #self is always first argument
        self.dimensions = dimensions
        self.windows = windows
        self.doors = doors
        self.flooring = flooring
        self.name = name
        self.contents = contents
    def nameOfRoom(self):
        print(self.name)
    def lowerCaseRoomName(self):
        self.name = self.name.lower()

room1 = Room("12x12x15", 2, 2, "tile", "The Streaming Room", ["Mic", "Mouse", "PC"])
#print(room1.dimensions)

# if room1.name == "The Streaming Room":
#     print("Yup, this is where we stream")

# for content in room1.contents:  #blank.blank is called dot notation
#     print(content)


#instance of a room
blakesRoom = Room("5x6x6", 0, 1, "stone", "PRIson cell", ["Empty Pot", "Pile of hay", "chains", "rat"])
# blakesRoom.nameOfRoom()

blakesRoom.nameOfRoom()
blakesRoom.lowerCaseRoomName()
blakesRoom.nameOfRoom()