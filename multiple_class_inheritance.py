from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, animal_type, number_of_legs):
        self.animal_type = animal_type
        self.number_of_legs = number_of_legs

    @abstractmethod
    def say_hello(self):
        pass

    def animal_details(self):
        return f"animal type: {self.animal_type}, number of legs: {self.number_of_legs}"

class Bird:
    def __init__(self, bird_type, can_fly):
        self.bird_type = bird_type
        self.can_fly = can_fly

    def bird_details(self):
        return f"Bird type: {self.bird_type}, can fly? {self.can_fly}"


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Parrot(Animal, Bird, Flyable):
    def __init__(self, animal_type, number_of_legs, bird_type, can_fly, name):
        Animal.__init__(self, animal_type, number_of_legs)
        Bird.__init__(self, bird_type, can_fly)
        self.name = name

    def print_parrot_details(self):
        print(f"Name: {self.name}, {Animal.animal_details(self)}\n{Bird.bird_details(self)}")

    def say_hello(self):
        print(f"Hello from the parrot {self.name}")

    def fly(self):
        print("Im flying now!")

if __name__ == "__main__":
    perry = Parrot('bird', 2, 'parrot', True, name="Perry")

    perry.print_parrot_details()
    perry.fly()
    perry.say_hello()

    animals = []
    for animal in animals:
        animal.say_hello()
