import copy

class Address:
    def __init__(self, street_address, city, country):
        self.street_address = street_address
        self.city = city
        self.country = country
    
    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def __str__(self):
        return f'{self.name} lives at {self.address}'

john = Person('John', Address('123, London Road', 'London', 'UK'))
print(john)
jane = john
jane.name = 'Jane'

print(john)
print(jane)

jane = copy.deepcopy(john)
jane.address.street_address = '1234, London Road'
print(jane)
print(john)