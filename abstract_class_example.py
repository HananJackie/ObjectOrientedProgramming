from abc import ABC, abstractmethod


class FlyingAnimal(ABC):

    @abstractmethod
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

    @abstractmethod
    def fly(self):
        print("I'm flying!!!")


class Bird(FlyingAnimal):
    def __init__(self, breed, age):
        super().__init__(breed, age)

    @abstractmethod
    def fly(self):
        super().fly()
        print('I am a bird!')

class Sparrow(Bird):
    def fly(self):
        super().fly()
        print('but not too far, I\'m little.')


bird = Sparrow('sparrow', 3)
bird.fly()
print(bird)