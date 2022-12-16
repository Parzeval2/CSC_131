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

    def reduce(self):
        gcd = 1
        minimum = min(abs(self.num), abs(self.den))

        #find common divisors
        for i in range(2, int(minimum + 1)):
            if self.num % i == 0 and self.den % i == 0:
                gcd = i

        #divide numerator and denominator by the GCD
        self.num /= gcd
        self.den /= gcd
        #if the numerator is 0, set the denominator to 1
        if (self.num == 0):
            self.den = 1
    def get_real(self):
        return float(self.num) / self.den
    def __str__(self):
        return "{}/{} ({})".format(self.num, self.den, self.get_real())

f1 = Fraction(1, 4)
print(f1)
f2 = Fraction(1, 0)
print(f2)