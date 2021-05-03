myDict = {'one': 'uno', 'two': 'dos', 'three': 'tres', 'four': 'cuarto'}


print('one' in myDict)
print('uno' in myDict.values())


for key in myDict:
    print(key)
    print(myDict[key])


print(all(myDict))
print(any(myDict))
print(len(myDict))
print(sorted(myDict, reverse=True))
print(sorted(myDict, key=len))