def capFirst(arr):
    resultArr = []
    for item in arr:
        resultArr.append(item.capitalize())
    return resultArr

print(capFirst(['ja', 'nee', 'test']))