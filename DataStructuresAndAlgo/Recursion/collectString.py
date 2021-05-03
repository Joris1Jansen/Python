def collectString(obj):
    newObj = []
    for key in obj:
        if type((obj[key])) is str:
            newObj.append(obj[key])
        if type((obj[key])) is dict:
            newObj = newObj + collectString(obj[key])
    return newObj

obj1 = {
    "num":'test1',
    "test": {
        "val": {
            "val": 'test3'
        }
    },
}

print(collectString(obj1))
