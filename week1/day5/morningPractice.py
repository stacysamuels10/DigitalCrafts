# Write a function that takes in a string of lowercase letters
# and returns the index of the string's first non-repeating character.
# If the input string does not have any non-repeating characters,
# your function should return -1.

letters = 'abcdcaf'

counter = {}
def practice (letters, counter):
    for letter in letters:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    for key in counter:
        if counter[key] == 1:
            print("You first non repeating charatcer is %s and is at index %d", key, letters.index(key))
            return
        else:
            print("-1")

practice (letters, counter)