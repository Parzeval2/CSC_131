#make a restaurant class
# 2 attributes, restaurant_name and cuisine_type
#method called describe_restaurant() that prints restaurant_name and cuisine_type
#method called open_restaurant() that prints a message indicating the restaurant is open
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open.")

Rotolos = Restaurant('Rotolos', 'Italian')
Rotolos.describe_restaurant()
Rotolos.open_restaurant()

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        ice_cream_flavors = ['Strawberry', 'Vanilla', 'Chocolate']
        self.ice_cream_flavors = ice_cream_flavors
    def flavors(self):
        print(self.ice_cream_flavors)

Braums = IceCreamStand('Braums', 'dessert')
Braums.flavors()