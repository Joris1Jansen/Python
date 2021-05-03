import numpy as np

twoDiArr = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

print(twoDiArr)

def accessElements(arr, rowIndex, colIndex):
    if rowIndex >= len(arr) or colIndex >= len(arr[0]):
        print('Incorrect index')
    else:
        print(arr[rowIndex][colIndex])

accessElements(twoDiArr, 3, 3)