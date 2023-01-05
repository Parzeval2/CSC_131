############################################################################
# name: Grant Cooper
# date: 1/5/2023
# description: Complex Number class that has many overloaded operators.
# couldnt get the output of the final division to be 2.999994 like it was in the paper but this works

###########################################################################

# Don't forget to name this file Complex.py and place it in the same
# folder as the provided ComplexTest.py file so that they can
# automatically find and use each other.

class Complex:
    # A constructor that takes two values for the real and imaginary
    # portions respectively. Default values for both parameters are 0.
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    # Accessors and Mutators for the instance variables
    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, real):
        self._real = real

    @property
    def imaginary(self):
        return self._imaginary

    @imaginary.setter
    def imaginary(self, imaginary):
        self._imaginary = imaginary

    # Overloaded mathematical operators i.e. ==, +, -, *, /

    def __add__(self, other):
        return f"{self.real + other.real} + {self.imaginary + other.imaginary}i"

    def __sub__(self, other):
        if self.imaginary - other.imaginary > 0:
            return f"{self.real - other.real} + {self.imaginary - other.imaginary}i"
        else:
            return f"{self.real - other.real} - {(self.imaginary - other.imaginary) * -1}i"

    def __mul__(self, other):
        return f"{self.real * other.real - self.imaginary * other.imaginary} + {self.real * other.imaginary + self.imaginary * other.real}i"

    # True div function has 2 variables that are the real part of the division and the imaginary part
    # it then combines them once each individual part is divided independently
    def __truediv__(self, other):
        real = self.real * other.real + self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary - self.imaginary * other.real
        divisor = other.real ** 2 + other.imaginary ** 2
        new_real = real / divisor
        new_imaginary = imaginary / divisor
        return f"{new_real} - {new_imaginary}i"

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    # Other functions e.g. reciprocal, conjugate, and __str__
    def reciprocal(self):
        return f"{self.real / ((self.real ** 2) + (self.imaginary ** 2))} - {(self.imaginary) / ((self.real ** 2) + (self.imaginary ** 2))}i"

    def conjugate(self):
        if self.imaginary > 0:
            return f"{self.real} - {self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary * -1}i"

    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} - {self.imaginary * -1}i"
        else:
            return f"{self.real} + {self.imaginary}i"
