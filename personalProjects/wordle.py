#steps for wordle
#a list of words
#program chooses a word at random
#while loop tries less than 6
# user choose a word, code reads over the word
#string deposited into a list
#iterate over the list
# if letter is in same index spot at chosen word, full correct
#if letter is in word but different index spot, half correct
# if not there at all, incorrect
import random
listOfWords = ['adult', 'agent', 'anger', 'apple', 'anger', 'apple', \
'award', 'basis', 'beach', 'birth', 'block', 'blood', 'board', \
'brain', 'bread', 'break', 'brown', 'buyer', 'cause', 'chain', \
'chair', 'chest', 'chief', 'child', 'china', 'claim', 'class', \
'clock', 'coach', 'coast', 'court', 'cover', 'cream', 'crime', \
'cross', 'crowd', 'crown', 'cycle', 'dance', 'death', 'depth',\
'doubt', 'draft', 'drama', 'dream', 'dress', 'drink', 'drive', \
'earth', 'enemy', 'entry', 'error', 'event', 'faith', 'fault', \
'field', 'fight', 'final' 'focus', 'force', 'frame', 'frank', \
'front', 'fruit', 'glass', 'grant', 'grass', 'green', 'group',\
'guide', 'heart','henry', 'horse', 'hotel', 'house', 'image', \
'index', 'input', 'issue', 'japan' 'jones', 'judge', 'knife', \
'laugh', 'layer', 'level', 'lewis', 'light', 'limit', 'lunch',\
'major', 'march', 'match', 'metal', 'model', 'money', 'month', \
'motor', 'mouth', 'music', 'night', 'noise', 'north', 'novel', \
'nurse', 'offer', 'order', 'other', 'owner', 'panel', 'paper',\
'party', 'peace', 'peter', 'phase', 'phone', 'piece', 'pilot',\
'pitch', 'place', 'plane', 'plant', 'plate', 'point', 'pound',\
'power', 'press', 'price', 'pride', 'prize', 'proof', 'queen',\
'radio', 'range', 'ratio', 'reply', 'right', 'river', 'round',\
'route', 'rugby', 'scale', 'scene', 'scope', 'score', 'sense',\
'shape', 'share', 'sheep', 'sheet', 'shift', 'shirt', 'shock',\
'sight', 'simon', 'skill', 'sleep', 'smile', 'smith', 'smoke',\
'sound', 'south', 'space', 'speed', 'spite', 'sport', 'squad',\
'staff', 'stage', 'start', 'state', 'steam', 'steel', 'stock',\
'stone', 'store', 'study', 'stuff', 'style', 'sugar', 'table',\
'taste', 'terry', 'theme', 'thing', 'title', 'total', 'touch',\
'tower', 'track', 'trade', 'train', 'trend', 'trial', 'trust',\
'truth', 'uncle', 'union', 'unity', 'value', 'video', 'visit',\
'voice', 'waste', 'watch', 'water', 'while', 'white', 'whole',\
'woman', 'world', 'youth']

wordleWord = 'black'
userGuess = ''
result = [0, 0, 0, 0, 0]

def wordArray (userGuess):
#[0, 2, 2, 0, 2]
    a = 0
    b = 0
    for a in range(len(userGuess)):
        if userGuess[a] not in wordleWord:
           result[a] = '0'
        for b in range(len(userGuess)):
            if userGuess[a] == wordleWord[b]:
                if a != b:
                    result[a] = '1'
                if a == b:
                    result[a] = '2'
    return result


def chooseCorrectWord (userGuess):
    if userGuess != wordleWord:
        wordArray(userGuess)
        print(result)

#chooseCorrectWord()

def numberOfGuesses ():
    i = 0
    counter = 5
    while i < 6:
        userGuess = input("What 5 letter word do you want?\n")
        if userGuess == wordleWord:
            print('You Win!')
            break
        if len(userGuess) == 5:
            chooseCorrectWord(userGuess)
            print(f"you have {counter} chances left")
            i+=1
            counter-=1
        if len(userGuess) != 5:
            print("Please choose a 5 letter word")
    print(wordleWord)

numberOfGuesses()


