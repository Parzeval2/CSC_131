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


################################################################
# ****    DO NOT MODIFY ANYTHING BELOW THIS POINT!    ****
################################# MAIN #########################

# Create three patient objects and print them out
p1 = Patient("Ben Dover", 22)
p2 = Patient("Helen Hywater", 16)
p3 = Patient("Amanda Lynn", 45)

print("\tName\t\tAge\tWeight")
print("-" * 40)
print("p1:\t{}\t{}\t{}".format(p1.name, p1.age, p1.weight))
print("p2:\t{}\t{}\t{}".format(p2.name, p2.age, p2.weight))
print("p3:\t{}\t{}\t{}".format(p3.name, p3.age, p3.weight))
print("-" * 40)

# Change their ages and print them out
p1.age = -5
p2.age = 100
p3.increaseAge()
p3.increaseAge()

print("p1:\t{}\t{}\t{}".format(p1.name, p1.age, p1.weight))
print("p2:\t{}\t{}\t{}".format(p2.name, p2.age, p2.weight))
print("p3:\t{}\t{}\t{}".format(p3.name, p3.age, p3.weight))
print("-" * 40)

# Change other instance variables and print them out
p1.weight = 2000
p2.name = "Justin Thyme"
p2.weight = 220
p3.weight = -50

print("p1:\t{}\t{}\t{}".format(p1.name, p1.age, p1.weight))
print("p2:\t{}\t{}\t{}".format(p2.name, p2.age, p2.weight))
print("p3:\t{}\t{}\t{}".format(p3.name, p3.age, p3.weight))
print("-" * 40)
