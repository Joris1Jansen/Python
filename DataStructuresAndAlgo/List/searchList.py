myList = [10, 20, 30, 40, 50, 60, 70, 80, 90]


# with the IN operator
if 200 in myList:
    print(myList.index(20))
else:
    print('Value does not exist in list')


# Linear function
def searchInList(list, value):
    for i in list:
        if i == value:
            return list.index(i)
    return print("No value found")

print(searchInList(myList, 300))