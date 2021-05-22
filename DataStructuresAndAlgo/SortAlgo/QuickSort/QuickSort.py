def partition(CustomList, low, high):
    i = low -1
    pivot = CustomList[high]
    for j in range(low, high):
        if CustomList[j] <= pivot:
            i += 1
            CustomList[i], CustomList[j] = CustomList[j], CustomList[i]
    CustomList[i+1], CustomList[high] = CustomList[high], CustomList[i+1]
    return (i+1)

def Quicksort(CustomList, low, high):
    if low < high:
        pi = partition(CustomList, low, high)
        Quicksort(CustomList, low, pi-1)
        Quicksort(CustomList, pi+1, high)

BasicList = [2, 6, 4, 8, 1, 3]
print(BasicList)
Quicksort(BasicList, 0, 5)
print(BasicList) 