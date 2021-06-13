class Journal:
    
    def __init__(self):
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, position):
        del self.entries[position]
    
    def __str__(self):
        return '\n'.join(self.entries)
    
    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    
    # def load(self, filename):
    #     pass

    # def low_from_web(self, uri):
    #     pass

class PersistanceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()




j = Journal()
j.add_entry('Shower')
j.add_entry('React')
print(f'Journal entries:\n{j}')
