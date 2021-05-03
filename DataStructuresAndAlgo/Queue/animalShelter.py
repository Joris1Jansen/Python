class AnimalShelter():

    def __init__(self):
        self.cats = []
        self.dogs = []
    
    def enqueue(self, animal, type):
        if type == 'Cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)
    
    def dequeueCat(self):
        if len(self.cats) == 0:
            return "No cats in the shelter"
        else:
            cat = self.cats.pop(0)
            return cat
    
    def dequeueDog(self):
        if len(self.dogs) == 0:
            return "No dogs in the shelter"
        else:
            dog = self.dogs.pop(0)
            return dog
    
    def dequeueAny(self):
        if len(self.dogs) == 0 and len(self.cats) == 0:
            return "No animals in the shelter" 
        elif len(self.cats) == 0:
            result = self.dogs.pop(0)
        else:
            result = self.cats.pop(0)
        return result


customQueue = AnimalShelter()
customQueue.enqueue('Cat1', 'Cat')
customQueue.enqueue('Cat2', 'Cat')
customQueue.enqueue('Dog1', 'Dog')
customQueue.enqueue('Dog2', 'Dog')
customQueue.enqueue('Cat3', 'Cat')
print(customQueue.dequeueAny())
