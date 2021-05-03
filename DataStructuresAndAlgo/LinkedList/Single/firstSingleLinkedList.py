class Node:
    def __init__(self, value=None):
        self.value = value
        self.next= None

class SinlgeLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

myLinkedList = SinlgeLinkedList()
node1 = Node(1)
node2 = Node(2)

myLinkedList.head = node1
myLinkedList.head.next = node2
myLinkedList.tail = node2