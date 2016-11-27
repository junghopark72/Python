class Human:
    country = 'South Korea'
    def __init__(self, name):
        self.name = name
    def eat_meal(self):
        print(self.name + ' is eating meal!!')
        
class BookReader(Human):
    def read_book(self):
        print(self.name + ' is reading Book!!')

class DrumPlayer(Human):
    def play_drum(self):
        print(self.name + ' is playing Drum!!')
