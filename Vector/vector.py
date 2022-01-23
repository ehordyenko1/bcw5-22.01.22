from math import hypot


class Vector:
    def __init__(self, x=0.0, y=0.0):
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = float(value)

    @y.setter
    def y(self, value):
        self._y = float(value)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def len(self):
        return hypot(self.x, self.y)

    def summary_numbers(self, other):
        self.x += other.x
        self.y += other.y


    def substract_numbers(self, other):
        self.x -= other.x
        self.y -= other.y

    def sum(self, other):
        result = self

        result.x += other.x
        result.y += other.y

        return result

    def substr(self, other):
        result = self

        result.x -= other.x
        result.y -= other.y

        return result

    def __str__(self):
        return f'({self.x}, {self.y})'


if __name__ == '__main__':
    vector = Vector(10, 15)
    vector1 = Vector(10,15)

    vector1.substr(vector)

    print(vector)
    print(vector1)