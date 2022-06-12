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
userGuess = ''
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

wordleWord = random.choice(listOfWords)

def compareWords ():
    i = 1
    counter = 5
    print(wordleWord)
    firstGuess = input("Choose a 5 letter word: \n")
    while i < 6:
        userGuess.lower() = firstGuess
        if userGuess.lower() == wordleWord:
            print("You win!")
            break
        if userGuess.lower() != wordleWord:
            a=0
            b = 0
            c = 0
            greenLetter = ''
            yellowLetter = ''
            for c in range(4):
                if userGuess[c] == wordleWord[c]:
                    greenLetter = greenLetter + userGuess[c]
                c +=1
            for a in range(4):
                for b in range(4):
                    if userGuess[a] == wordleWord[b]:
                        if a != b:
                            yellowLetter = yellowLetter + userGuess[a]
                    b += 1
                a += 1
            if greenLetter == '' and yellowLetter == '':
                print('No letters are in the correct spot')
            elif greenLetter == '' and yellowLetter != '':
                        print(f'No letters are in the correct spot, but {yellowLetter} are in the word but in a different spot')
            elif greenLetter != '' and yellowLetter != '':
                print(f"{greenLetter} are in the correct spot and {yellowLetter} are in the word but in a different spot")
            print("Try Again\n")
            userGuess = input(f"What is your next guess? You have {counter} chances left\n")
        i += 1
        counter -= 1

compareWords()