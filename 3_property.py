current_year = 2023


class Car:
    def __init__(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    def set_model(self, model):
        if model > current_year:
            model = current_year
        self.__model = model


car = Car(2008)
print(car.get_model())
car.set_model(2030)
print(car.get_model())


class Car:
    def __init__(self, model):
        self.__model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if model > current_year:
            model = current_year
        self.__model = model

    @model.deleter
    def model(self):
        del self.__model

    def __del__(self):
        del self


car = Car(2008)
print(car.model)
car.model = 2030
print(car.model)
