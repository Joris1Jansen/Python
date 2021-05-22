def InsertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i-1
        while j >=0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    print(customList)


BasicList = [2, 6, 4, 8, 1, 3]
# print(BasicList)
InsertionSort(BasicList)