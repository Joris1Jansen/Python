arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
    print(arr)
for i in range(0, 6):
    print(i)
    print('-')
    print(arr[i]) 
    # print(arr[i], end = " ")