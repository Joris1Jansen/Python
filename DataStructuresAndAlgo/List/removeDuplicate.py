myList = [1,1,2,2,3,4,5]

def removeDuplicates(lst):
    newList = []
    for i in lst:
        if i not in newList:
            newList.append(i)
    return newList

print(removeDuplicates(myList))