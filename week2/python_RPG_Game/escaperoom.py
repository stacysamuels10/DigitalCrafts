class EscapeRoom:
    def __init__(self, name, spellStrength, completedPuzzles, incorrectGuesses):
        self.name = name
        self.spellStrength = spellStrength
        self.completedPuzzles = completedPuzzles
        self.incorrectGuesses = incorrectGuesses

user = EscapeRoom("", 100, [], 0)

menu = "1. Look around the room, 2. Open my backpack, 3. Try the door, 4. Quit the game"