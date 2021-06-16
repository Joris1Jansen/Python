from abc import ABC
from enum import Enum, auto

class HotDrink(ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print('This tea is delicious')

class Coffee(HotDrink):
    def consume(self):
        print("This coffee is delicious")

class HotDrinksFactory(ABC):
    def prepare(self, amount):
        pass

class TeaFactory(HotDrinksFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil wat, '
                f'pour {amount}ml, enjoy!')
        return Tea()

class CoffeeFactory(HotDrinksFactory):
    def prepare(self, amount):
        print(f'Grind some beans, boil water, '
                f'pour {amount}ml, enjoy!')
        return Coffee()

def make_drink(types):
    if types == 'tea':
        return TeaFactory().prepare(200)
    elif types == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None

class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()
    
    factories = []
    initialized = False
    
    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instace = eval(factory_name)()
                self.factories.append((name, factory_instace))

    def make_drink(self):
        print('Available drinks: ')
        for f in self.factories:
            print(f[0])

        s = input(f'Please pick drink (0-{len(self.factories)-1}): ')
        idx = int(s)
        s = input(f'Specify amount: ')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)



if __name__ == '__main__':
    hdm = HotDrinkMachine()
    hdm.make_drink()
