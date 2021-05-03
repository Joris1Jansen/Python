def findMaxNumRec(sampleArray, n):
    if n == 1:
        return sampleArray[0]
    print(['sampleArray'], sampleArray[n-1])
    return max(sampleArray[n-1], findMaxNumRec(sampleArray, n-1))

a = [16, 4, 12, 7, 13, 10]
b = len(a)

print(findMaxNumRec(a, b))