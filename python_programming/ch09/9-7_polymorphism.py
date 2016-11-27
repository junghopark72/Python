class Developer:
    def __init__(self, name):
        self.name = name
    def coding(self):
        print(self.name + ' is a developer!!')

class PythonDeveloper(Developer):
    def coding(self):
        print(self.name + ' is a Python developer!!')

class JavaDeveloper(Developer):
    def coding(self):
        print(self.name + ' is a Java developer!!')
        
class CppDeveloper(Developer):
    def coding(self):
        super().coding()
        print(self.name + ' is a C++ developer!!')
