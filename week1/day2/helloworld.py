# Function
# 1. Function has a name
# 2. Function Arguments (sometimes)
# 3. Function has a Body

print("Hello World")

# Syntax in python for a function
# def
# functionName (doesnt matter what you call it)
# ():
# indent

# def sayHi():
#    print("Hi")
#    print("this is the body")

# Run a function
#sayHi()

#variables
# Variable types
# String "" anything inside is a string
"house" # string
"1" # string
"true" # string
"" # string
"print()" # string

# Boolean true/false on or the other
# cannot be both

# IS IT TRUTHY
True #has to be capital in py
# IS IT FALSY
False #has to be capital in py

# integers
number = 1 # whole number
bigNumber = 10000

# Float
floatNumber = 3.64

# List(python)/Arrays(javascript)

students = [
    "Jason", "Stacy", "West", "Carlos", "Amanda"
]
# Access a list by using the list index

print(students[1])

jobs = ["dev", "teacher", "nurse", "musician", "gamer"]
print(jobs[1])

# Dictionary(python)/Object(javascript)
# variable = {"key": value}

randomData = {
    "key": "value",
    "key": "value",
    "age": "old",
    "number": 1,
    "hot" : True,
    "students": ["Carlos", "Olivia"],
    "sorry": [
        {"name":
        {"name":
        {"name":
        ["1"]
        }
        }
}

]
}
#in order to access the value, i have to access the key
print(randomData["sorry"][0]["name"]["name"]["name"][0])

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian",
        "location": ["South America"]
    }
}
#name of pres
print(data["president"]["name"])
#location of pres
print(data["president"]["location"][0])