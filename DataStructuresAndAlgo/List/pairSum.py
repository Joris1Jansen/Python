myList = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]

def pairSum(lst, key):
    count = 0
    return sum(lst[count:count+1])
    # if sum(lst[count:count+1]) == key:
    #     count += 1
    #     return count
    # else:
    #     return pairSum(lst[1:],key)

print(pairSum(myList, 7))