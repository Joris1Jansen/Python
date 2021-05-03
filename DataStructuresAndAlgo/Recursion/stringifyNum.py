def stringifyNum(obj):
    newObj = obj
    for key in newObj:
        if type(obj[key]) is int:
            newObj[key] = str(newObj[key])
        if type(newObj[key]) is dict:
            newObj[key] = stringifyNum(newObj[key])
    return newObj

obj1 = {
    "num":1,
    "test": {
        "val":4
    },
}

print(stringifyNum(obj1))
