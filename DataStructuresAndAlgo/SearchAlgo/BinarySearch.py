import math

def BinarySearch(array, value):
    start = 0
    end = len(array)-1
    middle = math.floor((start + end) / 2)
    while array[middle] != value and start <= end:
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor((start + end) / 2)
    if array[middle] == value:
        return middle
    else:
        return -1
    


SimpleArray = [10, 20, 30, 40, 50, 60]
print(BinarySearch(SimpleArray, 40))

