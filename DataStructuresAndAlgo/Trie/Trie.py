class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insertString(self, word):
        current = self.root
        for i in word:
            char = i
            node = current.children.get(char)
            if node == None:
                node = TrieNode()
                current.children.update({char:node})
            current = node
        current.endOfString = True
        print("Successfully inserted")
    
    def search(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node
        
        if currentNode.endOfString == True:
            return True
        else:
            return False
    
def deleteString(root, word, index):
    if len(word) <= index:
        return True
    ch = word[index]
    currentNode = root.children.get(ch)
    if currentNode is None:
        return True
    canThisNodeBeDeleted = False
 
    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)        
    
    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True
    
    if currentNode.endOfString == True:
        deleteString(currentNode, word, index+1)
        return False
 
    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False    
 


newTrie = Trie()
newTrie.insertString('App')
newTrie.insertString('Appl')
# print(newTrie.search('App'))
# print(newTrie.search('Ap'))

deleteString(newTrie.root, 'App', 0)
print(newTrie.search('App'))