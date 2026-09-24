class Dog:
  def speak(self):
    return "Woof!"

class Cat:
  def speak(self):
    return "Meow!"

class Robot:
  def speak(self):
    return "Beep Boop!"


# Polymorphic Function: Accepts ANY object that has a speak() method
def make_it_speak(entity):
  print(entity.speak())


creatures = [Dog(), Cat(), Robot(), Robot(), Cat(), Dog()]
# Usage
for creature in creatures:
    make_it_speak(creature)