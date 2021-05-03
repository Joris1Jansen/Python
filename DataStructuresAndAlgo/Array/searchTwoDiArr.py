import numpy as np

twoDiArr = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDiArr)

def searchTwoDirArr(array, value):
     for i in range(len(array)):
         for j in range(len(array[0])):
             if array[i][j] == value:
                 return 'Value is located at '+str(i)+ ' ' + str(j)

print(searchTwoDirArr(twoDiArr, 10))