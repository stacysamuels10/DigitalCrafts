redList = [5, 5, 3, 9, 2]
blueList = [3, 6, 7, 2, 1]
blueandred = []
yetAnother = 0
slow1 = []
slowslow = 0

def maximumAmount(redList, blueList, yetAnother):
    for i in range(len(redList)):
        BlueAndRed = redList + blueList
        anotherBlueAndRed = sorted(BlueAndRed)
        anotherBlueAndRed.reverse()
    for i in range(len(redList)):
        yetAnother = yetAnother + anotherBlueAndRed[i]
    print(yetAnother)
maximumAmount(redList, blueList, yetAnother)

def minimumAmount(redList, blueList, yetAnother, slow1, slowslow):
    slowestRed = sorted(redList)
    slowestBlue = sorted(blueList)
    #print(slowestBlue)
    for i in range(len(redList)):
        if slowestRed[i] > slowestBlue[i]:
            slow1 = slow1 + slowestRed
            #print(slow1[i])
        if slowestBlue[i] > slowestRed[i]:
            slow1 = slow1 + slowestBlue
            #print(slow1[i])
        slowslow = slowslow + slow1[i]
    print(slowslow)

minimumAmount(redList, blueList, yetAnother, slow1, slowslow)