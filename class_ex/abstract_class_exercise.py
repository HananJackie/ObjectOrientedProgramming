from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def greets(self):
        pass

class Cat(Animal):
    def greets(self):
        print('Meow')

class Dog(Animal):
    def greets(self, another : 'Dog' = None):
        if another:
            print('Wooooof!')
        else:
            print('Woof!')

class BigDog(Dog):
    def greets(self, another : 'Dog' = None):
        if not another:
            print('Boof!')
        elif isinstance(another, BigDog):
            print('Boooooooooof!')
        elif isinstance(another, Dog):
            print('Boooof!')


if __name__ == '__main__':
    bonesy = Dog('Bonesy')
    rex = Dog('Rex')
    bonesy.greets()
    bonesy.greets(rex)

    bethoven = BigDog('Bethoven')
    lucky = BigDog('Lucky')

    bethoven.greets()
    bethoven.greets(bonesy)
    bethoven.greets(lucky)
