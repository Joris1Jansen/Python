myTuple = ( 'a', 'b', 'c', 'd', 'e')

print('b' in myTuple)
print('f' in myTuple)


def searchTuple(tuple, element):
    for i in tuple:
        if i == element:
            return tuple.index(i)
    return False

print(searchTuple(myTuple, 'f'))