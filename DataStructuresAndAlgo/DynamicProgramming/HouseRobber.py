def houseRobberTD(houses, currentIndex, tempDict):
    '''TOP DOWN'''
    if currentIndex >= len(houses):
        return 0
    else:
        if currentIndex not in tempDict:
            stealFirstHouse = houses[currentIndex] + houseRobberTD(houses, currentIndex + 2, tempDict)
            stealSecondHouse = houseRobberTD(houses, currentIndex+1, tempDict)
            tempDict[currentIndex] = max(stealFirstHouse, stealSecondHouse)
        return tempDict[currentIndex]

houses = [6, 7, 1, 30, 8, 2, 4]

print(houseRobberTD(houses, 0, {}))


def houseRobberBU(houses, currentIndex):
    '''BOTTOM UP'''
    tempArr = [0] * (len(houses)+2)
    for i in range(len(houses)-1, -1, -1):
        tempArr[i] =  max(houses[i]+tempArr[i+2], tempArr[i+1])
    return tempArr[0]

print(houseRobberBU(houses, 0))