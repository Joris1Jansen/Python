import queueLinkedList as queue

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
    

newBT = TreeNode('Drinks')
leftChild = TreeNode("Hot")

tea = TreeNode("Tea")
coffee = TreeNode("Coffee")

leftChild.leftChild = tea
leftChild.rightChild = coffee

rightChild = TreeNode("Cold")

newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "Binary tree does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Node is found " + nodeValue
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Value is not found in BT"

def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully inserted"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successfully inserted"

def getDeepestNode(rootNode):
    if not rootNode:
        return "Binary tree does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

        deepestNode = root.value
        return deepestNode

def deleteDepestNode(rootNode, deepestNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is deepestNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is deepestNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is deepestNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDepestNode(rootNode, dNode)
                return "Node is deleted succesfully"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Failed to delete the node"

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "Binary Tree is successfully deleted"



# levelOrderTraversal(newBT)
deleteNodeBT(newBT, "Hot")
levelOrderTraversal(newBT)
deleteBT(newBT)
levelOrderTraversal(newBT)
# newNode = getDeepestNode(newBT)
# deleteDepestNode(newBT, newNode)
# levelOrderTraversal(newBT)


# newNode = TreeNode("Cola")
# insertNodeBT(newBT, newNode)

# print(searchBT(newBT, "Cola"))
# levelOrderTraversal(newBT)
# deepestNode = getDeepestNode(newBT)
# print(deepestNode.data)