from BaseLinkedList import LinkedList

def removeDups(ll):
    '''
    With temporary buffer in the visited set()
    '''
    if ll.head is None:
        return
    else:
        curNode = ll.head
        visited = set([curNode.value])
        while curNode.next:
            if curNode.next.value in visited:
                curNode.next = curNode.next.next
            else:
                visited.add(curNode.next.value)
                curNode = curNode.next
        return ll


def removeDupsBufLess(ll):
    '''
    Withour a temporary buffer
    '''
    if ll.head is None:
        return
    else:
        curNode = ll.head
        while curNode:
            runner = curNode
            while runner.next:
                if runner.next.value == curNode.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            curNode = curNode.next
        return ll.head


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
removeDupsBufLess(customLL)
print(customLL)