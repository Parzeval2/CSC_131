class Dog:
    kind = 'canine'

    def __init__(self, dog_name):
        self.name = dog_name
        self.age = 0

    #accessor
    @property
    def age(self):
        return self._age


    #mutator
    @age.setter
    def age(self, age):
        if (age >= 0):
            self._age = age
d1 = Dog("hornswaggle")
d1.age = -5
print(d1.name)
print(d1.age)

#order of execution
#19
#4
#5
#6
#15
#16
#17
#20
#15
#16
#21
#22
#10
#11
