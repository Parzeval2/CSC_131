#fraction class
# - state
# --- numerator
# --- denominator
# - behavior
# --- addition
# --- subtraction
# --- rewrite as mixed number
# --- multiply
# --- divide
# --- display them

class Fraction:
    def __init__(self, num=0, den=1):
        self.num = num
        self.den = den

    @property
    def num(self):
        return self._num

    @property
    def den(self):
        return self._den

    @num.setter
    def num(self, value):
        self._num = value

    @den.setter
    def den(self, value):
        if (value != 0):
            self._den = value

f1 = Fraction(1, 4)
print("{}/{}".format(f1.num, f1.den))