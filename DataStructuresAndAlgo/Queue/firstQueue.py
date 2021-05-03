class Queue:

    def __init__(self):
        self.items = []
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of the Queue"

    def dequeue(self):
        if self.isEmpty():
            return "No element found in queue"
        else:
            return self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "No element found in queue"
        else:
            return self.items[0]
    
    def delete(self):
        self.items = None



newQueue = Queue()
newQueue.enqueue(1)
newQueue.enqueue(2)
newQueue.enqueue(3)
print(newQueue.isEmpty())
print(newQueue)
print(newQueue.dequeue()) 
print(newQueue.peek())
newQueue.delete()