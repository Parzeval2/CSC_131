class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, x):
        if (x < 10):
            self._x = -10
        elif (x > 10):
            self._x = 10
        else:
            self._x = x
    @y.setter
    def y(self, y):
        if (y < 10):
            self._y = -10
        elif (y > 10):
            self._y = 10
        else:
            self._y = y
p1 = Point()
print("p1=({}, {})".format(p1.x, p1.y))
p2 = Point(-50,50)