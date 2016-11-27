class BookReader:
    __country = 'South Korea'
    def update_country(self, country):
        self.__country = country
    def get_country(self):
        return self.__country
