import numpy as np

twoDiArr = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDiArr)

newArr = np.delete(twoDiArr, 0, axis=0)
print(newArr)