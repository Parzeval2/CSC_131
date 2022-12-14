class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

p1 = Point()
print("p1=({}, {})".format(p1.x, p1.y))