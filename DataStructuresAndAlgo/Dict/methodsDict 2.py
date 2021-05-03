myDict = {
    'name': 'Edy',
    'age': 26,
    'address': 'Londen',
    'education': 'master',
    'dog': True
}

mySecondDict = myDict.copy()

myDict.clear()
print(myDict)
print(mySecondDict)

newDict = {}.fromkeys([1, 2, 3], 0)
print(newDict)

print(mySecondDict.get('city'))

print(mySecondDict.items())

print(mySecondDict.keys())

print(mySecondDict.popitem())
print(mySecondDict)

print(mySecondDict.setdefault('dog', False))

print(mySecondDict.pop('dog'))
print(mySecondDict)

print(mySecondDict.values())

mySecondDict.update({'address': 'Amsterdam'})
mySecondDict.update({'cat': False})
print(mySecondDict)