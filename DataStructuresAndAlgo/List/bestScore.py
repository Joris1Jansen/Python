myList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]

def firstSecond(givenList):
    first = 0
    second = 0
    for i in givenList:
        if i > first:
            second = first
            first = i
        elif i > second:
            second = i
    return first, second

print(firstSecond(myList))