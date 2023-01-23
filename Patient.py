#############################################################
# author: Grant Cooper
# date: 12/14/2022
# desc: made a class for a patient and added constraints
#############################################################

# The patient class has a name, age, and weight. Only the name and age
# are provided as arguments to the constructor. The weight is set to 150
# by default for all objects. A Patient also has an increaseAge function
# that increases the age by 1.

class Patient:
    def __init__(self, name, age):
        self.name = name
        if (age < 0):
            self.age = 0
        self.age = age
        self.weight = 150

    def increaseAge(self):
        self.age += 1

    # age accessor
    @property
    def age(self):
        return self._age

    # weight accessor
    @property
    def weight(self):
        return self._weight

    # age setter
    @age.setter
    def age(self, age):
        if (age > 0):
            self._age = age
        else:
            self._age = 0

    # weight setter
    @weight.setter
    def weight(self, weight):
        if (weight < 0):
            self._weight = 150
        elif (weight > 1400):
            self._weight = 150
        else:
            self._weight = weight


class In(Patient):
    def __init__(self, name, age, stay=5):
        super().__init__(name, age)
        self.name = name
        self.age = age
        self.stay = stay

    @property
    def stay(self):
        return self._stay

    @stay.setter
    def stay(self, stay):
        if (stay < 0):
            self._stay = 0
        else:
            self._stay = stay

    def __str__(self):
        return f"IN-  {self.name:<16} {self.age:<3} {self.weight:<5} {self.stay:<1}"

class Out(Patient):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return f"OUT- {self.name:<16} {self.age:<3} {self.weight:<5}"

class ICU(In):
    def __init__(self, name, age):
        super().__init__(name, age)

    days = 5

class CheckUp(Out):
    def __init__(self, name, age):
        super().__init__(name, age)