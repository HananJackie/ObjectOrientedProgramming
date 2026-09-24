from overrides import overrides

class Shape:
  def area(self):
    raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @overrides
    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @overrides
    def area(self):
        return 3.14159 * (self.radius**2)


# Polymorphic Processing of a List
shapes = [Rectangle(10, 20), Circle(5), Rectangle(3, 4)]

for shape in shapes:
  # Calls the specific area() implementation for each object
  print(f"Area: {shape.area():.2f}")