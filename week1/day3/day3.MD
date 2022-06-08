# Lists and Time and Space Complexity

array = []
list = []
Access things inside of list using an index
List has to always be next to each other in the computer
reading the index by saying "O(h) of 1" array[0]
inserting something you pronounce "O(h) of n" array[0] n = size of array or list

time and space complexity asks how big is the data and how long will it take to put the data in there

always prepare for the worst case scenario

Big O are constants and is instant

```
listOfStudents = ["a", "b", "c"]

#want to print out a, b, c, d
listOfStudents.append("d")
```

if i want a new list from the old list

```
newList.extend(listOfStudents)
```

or

```
newList = newList + listOfStudents
```

or in a for loop

```

for student in listOfStudents:
    newList.append(listofStudents[])
```
