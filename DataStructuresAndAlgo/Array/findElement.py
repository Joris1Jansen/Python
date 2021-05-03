from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])

def searchElement(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "Element does not exist in array"

print(searchElement(arr1, 3))