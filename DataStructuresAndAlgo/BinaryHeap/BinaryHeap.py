class Heap:

    def __init__(self, size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1
    
    def heapifyInsert(self, index, heapType):
        parentIndex = int(index/2)
        if index <= 1:
            return
        if heapType == 'Min':
            if self.customList[index] < self.customList[parentIndex]:
                temp = self.customList[index]
                self.customList[index] = self.customList[parentIndex]
                self.customList[parentIndex] =  temp
            self.heapifyInsert(parentIndex, heapType)
        elif heapType == 'Max':
            if self.customList[index] > self.customList[parentIndex]:
                temp = self.customList[index]
                self.customList[index] = self.customList[parentIndex]
                self.customList[parentIndex] =  temp
            self.heapifyInsert(parentIndex, heapType)
    
    def insertNode(self, nodeValue, heapType):
        if self.heapSize + 1 == self.maxSize:
            return "Binary heap is full"
        self.customList[self.heapSize + 1] = nodeValue
        self.heapSize += 1
        self.heapifyInsert(self.heapSize, heapType)
        return "Value is successfully inserted"
    
    def peakOfHeap(self):
        if not self.customList:
            return
        else:
            return self.customList[1]

    def sizeOfHeap(self):
        if not self.customList:
            return
        else:
            return self.heapSize
    
    def levelOrderTraversal(self):
        if not self.customList:
            return
        else:
            for i in range(1, self.heapSize+1):
                print(self.customList[i])
    
    def heapifyExtract(self, index, heapType):
        leftIndex = index * 2
        rightIndex = index * 2 + 1
        swapChild = 0

        if self.heapSize < leftIndex:
            return
        elif self.heapSize == leftIndex:
            if heapType == 'Min':
                if self.customList[index] > self.customList[leftIndex]:
                    temp = self.customList[index]
                    self.customList[index] = self.customList[leftIndex]
                    self.customList[leftIndex] =  temp
                return
            else:
                if self.customList[index] < self.customList[leftIndex]:
                    temp = self.customList[index]
                    self.customList[index] = self.customList[leftIndex]
                    self.customList[leftIndex] =  temp
                return     
        else:
            if heapType == 'Min':
                if self.customList[leftIndex] < self.customList[rightIndex]:
                    swapChild = leftIndex
                else:
                    swapChild = rightIndex
                if self.customList[index] > self.customList[swapChild]:
                    temp = self.customList[index]
                    self.customList[index] = self.customList[swapChild]
                    self.customList[swapChild] =  temp
            else:
                if self.customList[leftIndex] > self.customList[rightIndex]:
                    swapChild = leftIndex
                else:
                    swapChild = rightIndex
                if self.customList[index] < self.customList[swapChild]:
                    temp = self.customList[index]
                    self.customList[index] = self.customList[swapChild]
                    self.customList[swapChild] =  temp
            self.heapifyExtract(swapChild, heapType)

    def extractNode(self, heapType):
        if self.heapSize == 0:
            return
        else:
            extractNode = self.customList[1]
            self.customList[1] = self.customList[self.heapSize]
            self.customList[self.heapSize] = None
            self.heapSize -= 1
            self.heapifyExtract(1, heapType)
            return extractNode
    
    def deleteEntireBP(self):
        self.customList = None





newHeap = Heap(5)
newHeap.insertNode(4, "Max")
newHeap.insertNode(5, "Max")
newHeap.insertNode(2, "Max")
newHeap.insertNode(1, "Max")
newHeap.extractNode('max')
print(newHeap.levelOrderTraversal())