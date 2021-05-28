def Merge(CustomList, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = CustomList[l+i]
    
    for j in range(0, n2):
        R[j] = CustomList[m+1+j]
    
    i = 0 
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            CustomList[k] = L[i]
            i += 1
        else:
            CustomList[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        CustomList[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        CustomList[k] = R[j]
        j += 1
        k += 1

def MergeSort(CustomList, l ,r):
    if l < r:
        m = (l+(r-1))//2
        MergeSort(CustomList, l, m)
        MergeSort(CustomList, m+1, r)
        Merge(CustomList, l, m, r)
    return CustomList


BasicList = [2, 6, 4, 8, 1, 3]
# print(BasicList)
print(MergeSort(BasicList,0 ,5))