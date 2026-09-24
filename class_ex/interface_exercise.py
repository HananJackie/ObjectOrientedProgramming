from abc import ABC


class Movable(ABC):
    def move_up(self): pass
    def move_down(self): pass
    def move_left(self): pass
    def move_right(self): pass


class MovablePoint(Movable):
    def __init__(self, x, y, speed_x, speed_y):
        self._x = x
        self._y = y
        self._speed_x = speed_x
        self._speed_y = speed_y

    def __repr__(self):
        return f'({self._x}, {self._y} speed=({self._speed_x}, {self._speed_y}))'

    def move_up(self):
        self._y -= self._speed_y

    def move_down(self):
        self._y += self._speed_y

    def move_left(self):
        self._x -= self._speed_x

    def move_right(self):
        self._x += self._speed_x

if __name__ == "__main__":
    point = MovablePoint(100, 100, 5, 5)
    print(point)
    point.move_up()
    print(point)
    point.move_up()
    point.move_up()
    point.move_right()
    point.move_right()
    print(point)
    print(point.x)
