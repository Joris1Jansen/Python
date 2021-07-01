class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None
    
    def __str__(self):
        return f'{self.name} is born on {self.date_of_birth} ' +\
                'working as a {self.position}'
    
    @staticmethod
    def new():
        return PersonBuilder()

class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person

class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self

class PersonJobBuilder(PersonInfoBuilder):
    def position(self, job):
        self.person.position = job
        return self

pb = PersonJobBuilder()
me = pb\
    .called('Joris').build()

print(me)