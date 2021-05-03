myList = ([1, 2, 3, 4, 6])

def missingNumber(myList, totalCount):
    sum1 = (totalCount * (totalCount + 1))/2
    sum2 = sum(myList)

    return sum1 - sum2

print(missingNumber(myList, 6))