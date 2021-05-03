def capWords(arr):
    resultArr = []
    if len(arr) == 0:
        return resultArr
    resultArr.append(arr[0].upper())
    return resultArr + capWords(arr[1:])

arr = ['ja', 'nee', 'test']

print(capWords(arr))