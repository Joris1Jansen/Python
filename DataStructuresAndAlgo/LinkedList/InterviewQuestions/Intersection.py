from BaseLinkedList import LinkedList, Node

def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False
    
    lenA = len(llA)
    lenB = len(llB)

    shortest = llA if lenA < lenB else llB
    longest = llB if lenA < lenB else llA

    diff = len(longest) - len(shortest)
    longerNode = longest.head
    shorterNode = shortest.head

    for i in range(diff):
        longerNode = longerNode.next
    
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    
    return longerNode

#helper addition method
def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode

    llB.tail.next = tempNode
    llB.tail = tempNode

llA = LinkedList()
llA.generate(3, 0, 10)

llB = LinkedList()
llB.generate(4, 0, 10)

addSameNode(llA, llB, 14)
addSameNode(llA, llB, 11)

print(llA)
print(llB)

print(intersection(llA, llB))