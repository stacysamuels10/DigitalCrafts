#sum the numbers
#create a list of numbers and print the sum

list1 = [10, 20, 30, 40,]
total = 0

for number in range(0, len(list1)):
        total = total + list1[number]
print(total)

#largest Number
#create a list of numbers, print largest

list2 = [10, 20, 30, 40]
list2.sort
print(list2[-1])

#smallest number
#create a list of numbers, print smallest

list3 = [10, 20, 30, 40]
list3.sort
print(list3[0])

#even numbers
#create a list and print each number that is even

list4 = [10, 20, 35, 41]

for number in list4:
    if number %2 == 0:
        print(number)

#positive number I
#create a list of numbers, print each number that is great than zero

list5 = [ -1, -10, 5, 23]

for number in list5:
    if number > 0:
        print(number)


#positive number II
list5 = [ -1, -10, 5, 23]
newList5 = []

for number in list5:
    if number > 0:
        newList5.append(number)
print(newList5)

#multiply a list
#create a list of numbers and a single factor (also a number), create a new list

list6 = [10, 20, 30, 40]
singleFactor = 10
newList6 = []

for number in list6:
    newList6.append(number*singleFactor)
print(newList6)

#reverse a string
#given a string, print reversed

word = "Stacy" [::-1]
print(word)