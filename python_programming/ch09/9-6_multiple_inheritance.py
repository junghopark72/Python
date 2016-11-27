class Human:
    country = 'South Korea'
    def __init__(self, name):
        self.name = name
    def eat_meal(self):
        print(self.name + ' is eating meal!!')

class Developer:
    def coding(self):
        print(self.name + ' is a developer!!')

class ProgramBookWriter(Human, Developer):
    def write_book(self):
        print(self.name + ' is writing book!!')
