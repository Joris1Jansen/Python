myList = [1, 2, 3, 4, 5, 6, 7]
print(myList)


# Updating
myList[2] = 33
print(myList) 


# Inserting
myList.insert(3, 999999)
print(myList)


# Append
myList.append(123)
print(myList)


# Extend
mySecondList = [11, 12, 13, 14]
myList.extend(mySecondList)
print(myList)


# Slice
print(myList[0:2])
print(myList[:2])
print(myList[2:])


# Update
myList[0:2] = ['a', 'b']
print(myList)


# Delete with pop
print(myList)
print(myList.pop())
print(myList)


# Delete with delete
del myList[1]
print(myList)

# Delete with remove
myList.remove('a')
print(myList)
