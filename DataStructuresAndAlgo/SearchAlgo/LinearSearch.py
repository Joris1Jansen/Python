def LinearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1

BasicArray = [20, 40, 10, 50, 60, 30]

print(LinearSearch(BasicArray, 300))