class Creature:
    _strength = 0
    _agility = 1
    _intelligence = 2

    def __init__(self):
        self.stats = [10, 10, 10] # Array backed property or List backed property
        # self.strength = 10
        # self.agility = 10
        # self.intelligence = 10
    
    @property
    def strength(self):
        return self.stats[Creature._strength]
    
    @strength.setter
    def strength(self, value):
        self.stats[Creature._strength] = value
    
    @property
    def agility(self):
        return self.stats[Creature._agility]
    
    @agility.setter
    def agility(self, value):
        self.stats[Creature._agility] = value
    
    @property
    def intelligence(self):
        return self.stats[Creature._intelligence]

    @intelligence.setter
    def intelligence(self, value):
        self.stats[Creature._intelligence] = value

    @property
    def sum_of_stats(self):
        return sum(self.stats)
        # return self.strenght + self.agility + self.intelligence
    
    @property
    def max_stat(self):
        return max(self.stats)
        # return max(
        #     self.strength,
        #     self.intelligence,
        #     self.agility
        # )
    
    @property
    def average(self):
        return float(sum(self.stats)/len(self.stats))