class Vector:
    def __init__(self, *args):
        self.coordinates = args

    def __add__(self, other):
        if len(other) != len(self):
            raise ValueError('Both vectors should be of the same length')

        new_coordinates = []
        for c1, c2 in zip(self.coordinates, other.coordinates):
            new_coordinates.append(c1+c2)
        return Vector(*new_coordinates)

    def __str__(self):
        return f'<{', '.join([str(c) for c in self.coordinates])}>'

    def __eq__(self, other):
        if len(other) != len(self):
            raise ValueError('Both vectors should be of the same length')

        for c1, c2 in zip(self.coordinates, other.coordinates):
            if c1 != c2:
                return False
        return True

    def __len__(self):
        return len(self.coordinates)

if __name__ == "__main__":
    v1 = Vector(1,2,3,4,5, 7)
    v2 = Vector(1,2,5,6,7)
    v = v1 + v2

    print(v1)
    print(v2)
    print(v)
    print(v1 == v2)
