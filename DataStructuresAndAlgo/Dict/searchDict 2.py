myDict = {
    'name': 'Edy',
    'age': 26,
    'address': 'Londen'
}

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'value does not exist'

print(searchDict(myDict, 26))