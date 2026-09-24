from abc import ABC, abstractmethod


class Soundable(ABC):

    @abstractmethod
    def make_sound(self): pass


class Dog(Soundable):
    def __init__(self, breed, name, age, owner_name):
        self.breed = breed
        self.name = name
        self.age = age
        self.owner_name = owner_name

    def make_sound(self):
        print("Woof Woof!")

class MetalPan(Soundable):
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def make_sound(self):
        print('pamtanbrahlzskdjfl')

class Object:
    def __init__(self, **kwargs):
        # Automatically set whatever keyword arguments are passed in
        self.__dict__.update(kwargs)

    def __repr__(self):
        # Pretty print the internal attributes
        return f"Object({self.__dict__})"

def make_sound(s: Soundable):
    s.make_sound()

if __name__ == "__main__":
    doggy = Dog('belgian shepard', 'Erru', 4, 'Danny')
    pan = MetalPan('Tefal', 100.50)
    make_sound(doggy)
    make_sound(pan)

    general_obj = Object(name='General Object', description='an amorphic object', age=10000000000)
    general_obj.make_sound = lambda: print('A general object sound')
    make_sound(general_obj)
