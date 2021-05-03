myList = [[1,2,3],[4,5,6],[7,8,9]]

def sumDiagonal(arr):
    length = len(arr)
    r1 = 0
    for i in range(length):
        r1 += arr[i][length - i - 1]
    return(r1)


print(sumDiagonal(myList))
