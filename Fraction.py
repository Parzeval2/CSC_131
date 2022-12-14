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
        if (den == 0):
            den = 1
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

    def get_real(self):
        return float(self.num) / self.den
    def __str__(self):
        return "{}/{} ({})".format(self.num, self.den, self.get_real())

f1 = Fraction(1, 4)
print(f1)
f2 = Fraction(1, 0)
print(f2)