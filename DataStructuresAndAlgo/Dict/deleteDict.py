myDict = {
    'name': 'Edy',
    'age': 26,
    'address': 'Londen',
    'education': 'master'
}


myDict.pop('name')
print(myDict)


myDict.popitem()
print(myDict)


del myDict['address']
print(myDict)


myDict.clear()
'''or use del myDict'''

print(myDict)
