myDict = {
    'name': 'Edy',
    'age': 26,
    'address': 'Londen'
}

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

traverseDict(myDict)