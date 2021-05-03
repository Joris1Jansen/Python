class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.prev = newNode
        return "CDLL is create successfully"
    
    def insertCDLL(self, value, location):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
            return "Node has been successfully inserted"
    
    def traverseCDLL(self):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    def reverseTraverseCDLL(self):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    def searchCDLL(self, nodeValue):
        if self.head is None:
            return "The CDLL does not exist"
        else: 
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                if tempNode == self.tail:
                    return "Value does not exist in CDLL"
                tempNode = tempNode.next




cdll = CircularDoubleLinkedList()
cdll.createCDLL(5)
print([node.value for node in cdll])

cdll.insertCDLL(0,0)
cdll.insertCDLL(1,1)
cdll.insertCDLL(10,2)

print([node.value for node in cdll])

cdll.traverseCDLL()
cdll.reverseTraverseCDLL()
print(cdll.searchCDLL(10))