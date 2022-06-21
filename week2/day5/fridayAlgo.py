array = [5, 1, 4, 2]

products = [1 for _ in range(len(array))]

for i in range(len(array)):
    runningProduct = 1
    for j in range(len(array)):
        if i != j:
            runningProduct *= array[j]
    products[i] = runningProduct    
    

print(products)

#every algorith sort from least to greatest, 
#starting from front, back, middle, end to help you sove the problem