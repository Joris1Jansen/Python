class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The dll is created successfully"
    
    def insertDLL(self, nodeValue, location):
        if self.head == None:
            print("The node can not be inserted")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    def traverseDLL(self):
        if self.head == None:
            print("There is not any element to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
    
    def reverseTraverseDLL(self):
        if self.head == None:
            print("There is no element to traverse")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    def searchDLL(self, nodeValue):
        if self.head == None:
            print("There is no element to search")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return "The node does not exist in this list"



dll = DoublyLinkedList()
print([node.value for node in dll])

dll.createDLL(5)
dll.insertDLL(0,0)
dll.insertDLL(10,1)
dll.insertDLL(2,2)

print([node.value for node in dll])

# dll.traverseDLL()
# dll.reverseTraverseDLL()

print(dll.searchDLL(6))