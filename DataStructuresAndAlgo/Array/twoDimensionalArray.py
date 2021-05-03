# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

import numpy as np

twoDiArr = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

print(twoDiArr)


# Insert column (axis=1) or row (axis=0)

newTwoDiArr = np.insert(twoDiArr, 1, [1, 2, 3, 4], axis=0)
print(newTwoDiArr)


newTwoDiArr = np.append(twoDiArr, [[1, 2, 3, 4]], axis=0)
print(newTwoDiArr)
