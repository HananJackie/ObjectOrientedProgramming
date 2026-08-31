import pprint

class Car:
    def __init__(self, type, model="Unknown", color="Unknown", speed=0):
        self.__type = type
        self.__model = model
        self.__color = color
        self.__speed = speed

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, new_type):
        self.__type = new_type

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    def accelerate(self, required_speed):
        while self.__speed < required_speed:
            print("accelerating..", f'current speed: {self.__speed}')
            self.__speed += 1

    def print(self):
        print(f'type: {self.__type}\nmodel: {self.__model}\ncolor: {self.__color}\nspeed: {self.__speed}\n')

    def __str__(self):
       return f'type: {self.__type}\nmodel: {self.__model}\ncolor: {self.__color}\nspeed: {self.__speed}\n'


if __name__ == '__main__':
    car = Car("Toyota", "x123", "Red", 30)
    print(f'This is car type {car.type}')
    car.model = "Rd43"
    print(f'This is car type {car.model}')



