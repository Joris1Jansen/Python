def isBalancedHelper(root):
    if root is None:
        return 0
    leftHeight = isBalancedHelper(root.left)
    if leftHeight == -1:
        return -1
    rightHeigt = isBalancedHelper(root.right)
    if rightHeigt == -1:
        return -1
    if abs(leftHeight - rightHeigt)>1:
        return -1
    
    return max(leftHeight, rightHeigt) +1

def isBalanced(root):
    return isBalancedHelper(root) > 1

class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

N1 = Node("N1")
N2 = Node("N2")
N3 = Node("N3")
N4 = Node("N4")
N5 = Node("N5")
N6 = Node("N6")
N7 = Node("N7")

N1.left = N2
N1.right = N3
N2.left = N4
N2.right = N5
N3.right = N6
N6.right = N7

print(isBalanced(N1))