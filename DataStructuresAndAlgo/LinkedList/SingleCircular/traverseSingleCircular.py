class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSingleLinkedList:
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
    
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "CSLL is created"
    
    def insertCSLL(self, value, location):
        if self.head is None:
            return "The linkedlist does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "Insertion completed"
    
    def traverseCSLL(self):
        if self.head is None:
            return "The linked list does not contain any node"
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break
    


csll = CircularSingleLinkedList()
csll.createCSLL(1)
csll.insertCSLL(0, 0)
csll.insertCSLL(2, 1)
csll.insertCSLL(3, 2)
csll.traverseCSLL()

print([node.value for node in csll])