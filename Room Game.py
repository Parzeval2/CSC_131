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

    @exits.setter
    def exits(self, value):
        self._name = value

    # name Accessor and mutator
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # exit location accessor and mutator
    @property
    def exit_location(self):
        return self._exit_location

    @exit_location.setter
    def exit_location(self, value):
        self._exit_location = value

    # item description accessor and mutator
    @property
    def item_description(self):
        return self._item_description

    @item_description.setter
    def item_description(self, value):
        self._item_description = value

    # item accessor and mutator
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    # grabbables accessor and mutator
    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

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
        s = f"You are in {self.name}.\nYou see: "
        for item in self.items:
            s += f"{item} "
        s += "\n"
        # exits from the room
        s += "Exits: "
        for exit in self.exits:
            s += f"{exit} "
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
    r1.add_item("Table", "Its made of oak, and a golden key rests on top")

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
    status = f"{current_room}\nYou are carrying: {inventory}"

    # If the current room is None, the player is dead
    if current_room is None:
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
    if action in ["quit", "exit", "bye"]:
        break

    # set a default response
    response = "I dont understand. Try <verb> <noun>. Valid verbs are go, look, and take."

    # split the user input into words and store the words in a list
    words = action.split()

    # the game only understands 2 word inputs
    if (len(words) == 2):
        verb = words[0]
        noun = words[1]

        # the verb is go
        if verb == "go":
            # set a default response
            response = "Invalid exit."

            # check for valid exits in the current room
            for i in range(len(current_room.exits)):
                # a valid exit is found
                if (noun == current_room.exits[i]):
                    # change the current room
                    current_room = current_room.exit_locations[i]
                    # set the response
                    response = "Room Changed."
                    # no need to check for more exits
                    break
        elif verb == "look":
            response = next(
                (
                    current_room.items_description[i]
                    for i in range(len(current_room.items))
                    if (noun == current_room.items[i])
                ),
                "I don't see that item.",
            )
        elif verb == "take":
            # set a default response
            response = "I don't see that item."

            # check for valid grabbable items in the current room
            for grabbable in current_room.grabbables:
                # a valid grabbable item is found
                if (noun == grabbable):
                    # add the grabbable item to the player's inventory
                    current_room.del_grabbable(grabbable)
                    # set the response
                    response = "Item Grabbed!"
                    break

    # display the response
    print(f"\n{response}")
