class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    
    def push(self, value):
        if self.isFull():
            return "the stack is full"
        else:
            self.list.append(value)
            return "Element has been successfully inserted"
    
    def pop(self):
        if self.isEmpty():
            return "Nothin to pop from the stack"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.list[len(self.list)-1]

    def delete(self):
        self.list = None

newStack = Stack(5)

newStack.isEmpty()

newStack.push(1)
newStack.push(2)
newStack.push(3)

print(newStack.pop())
print(newStack.peek())