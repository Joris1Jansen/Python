class PlateStack():
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
    
    def __str__(self):
        return self.stacks
    
    def push(self, item):
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])
    
    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()

    def pop_at(self, stackNunber):
        if len(self.stacks[stackNunber]) > 0:
            return self.stacks[stackNunber].pop()
        else:
            return None


customStack = PlateStack(2)
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.pop())