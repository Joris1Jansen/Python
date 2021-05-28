def Heapify(CustomList, n, i):
    smallest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and CustomList[l] < CustomList[smallest]:
        smallest = l

    if r < n and CustomList[r] < CustomList[smallest]:
        smallest = r
    
    if smallest != i:
        CustomList[i], CustomList[smallest] = CustomList[smallest], CustomList[i]
        Heapify(CustomList, n, smallest)

def HeapSort(CustomList):
    n = len(CustomList)
    for i in range(int(n/2)-1, -1, -1):
        Heapify(CustomList, n, i)
    
    for i in range(n-1, 0, -1):
        CustomList[i], CustomList[0] = CustomList[0], CustomList[i]
        Heapify(CustomList, i, 0)
    CustomList.reverse()

BasicList = [2, 6, 4, 8, 1, 3]
print(BasicList)
HeapSort(BasicList)
print(BasicList)  