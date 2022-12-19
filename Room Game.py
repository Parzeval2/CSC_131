class Room:
    def __init__(self, name):
        self.name = name
        self.exits = []
        self.exit_locations = []
        self.items = []
        self.item_descriptions = []
        self.grabbables = []

    # getters and setters
    @property
    def exits(self):
        return self._name

    @name.setter
    def self(self, value):
        self._name = value

    # TODO:
    # Create accessors and mutators for exits, exit_locations, items, item_descriptions, and grabbables

    # adds an exit to the room
    # exit is a string
    # room is an instance of a Room
    def add_exit(self, exit, room):
        self.exits.append(exit)
        self.exit_locations.append(room)

    # adds an item to the room
    # item is a string
    # desc is a string that describes the item
    def add_item(self, item, desc):
        self.items.append(item)
        self.item_descriptions.append(desc)

    # adds a grabbable item to the room
    # item is a string
    def add_grabbable(self, item):
        self.grabbables.append(item)

    # removes a grabbable item from the room
    # item is a string
    def del_grabbable(self, item):
        self.grabbables.remove(item)

    # return a string description of the room
    def __str__(self):
        # room name
        s = "You are in {}.\n".format(self.name)
        # items in the room
        s += "You see: "
        for item in self.items:
            s += item + " "
        s += "\n"
        # exits from the room
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "
        return s


# make the rooms
def create_rooms():
    global current_room

    # create the rooms and give them meaningful names
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")

    # create room 1
    r1.add_exit("East", r2)
    r1.add_exit("South", r3)
    r1.add_grabbable("Key")
    r1.add_item("Chair", "Its made of wicker")
    r1.add_item("Table", "Its made of oak, and a golden key rests on top"

    # create room 2
    r2.add_exit("West", r1)
    r2.add_exit("South", r4)
    r2.add_item("Rug", "It should probably be vacuumed")
    r2.add_item("fireplace", "Cold and full of ashes")

    # create room 3
    r3.add_exit("North", r1)
    r3.add_exit("East", r4)
    r3.add_grabbable("book")
    r3.add_item("Bookshelves", "Empty with no books")
    r3.add_item("Statue", "Nothing special about it")
    r3.add_item("Desk", "A statue rests on the desk, along with a book")

    # create room 4
    r4.add_exit("North", r2)
    r4.add_exit("West", r3)
    r4.add_exit("South", None)
    r4.add_grabbable("6-Pack")
    r4.add_item("Brew_Rig", "Someone was brewing some sort of delicious beverage. A 6-Pack rests next to it")

    # set the current_room
    current_room = r1
    # better death in pdf


def death():
    print("You got dead")


# Start the game
inventory = []
create_rooms()

# game loop (Play forever until the player dies or asks to quit)
while True:
    status = "{}\nYou are carrying: {}".format(current_room, inventory)

    # If the current room is None, the player is dead
    if (current_room = None):
        death()
        break

    # display status
    print("====================================")
    print(status)
    print("====================================")

    # prompt for player input
    # game supports simple language of <verb> <noun>
    # valid verbs are go, look, and take
    # valid nouns depend on the verb
    action = input("What to do? ")
    action = action.lower()

    # exit the game if the player types 'quit', 'exit', or 'bye'
    if (action == "quit" or action == "exit" or action == "bye"):
        break
