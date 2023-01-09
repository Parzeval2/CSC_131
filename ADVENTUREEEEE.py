class Room:
    # constructor
    def __init__(self, name):
        self.name = name
        self.exits = []
        self.exit_locations = []
        self.items = []
        self.item_descriptions = []
        self.grabbables = []

    # getters and setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # adds an exit to the room
    # exit is a string
    # room is an instane of a room
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
    def add_grabbables(self, item):
        self.grabbables.append(item)

    # removes a grabbable item from the room
    # item is a string
    def del_grabbable(self, item):
        self.grabbables.remove(item)

    # return a string description of the room
    def __str__(self):
        # first, the room name
        s = "You are in {}.\n".format(self.name)
        # next, the items in the room
        s += "You see: "
        for item in self.items:
            s += item + " "
        s += "\n"
        # last, the exits from the room
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "
        return s


def create_rooms():
    global current_room

    # create the rooms and give them meaningful names
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")

    # create room 1
    r1.add_exit("east", r2)
    r1.add_exit("south", r3)
    r1.add_grabbables("key")
    r1.add_item("chair", "It's made of wicker.")
    r1.add_item("table", "It's made of oak and a golden key rests on top.")

    # create room 2
    r2.add_exit("west", r1)
    r2.add_exit("south", r4)
    r2.add_item("rug", "It should probably be vacummed.")
    r2.add_item("fireplace", "Cold and full of ashes.")

    # create room 3
    r3.add_exit("north", r1)
    r3.add_exit("east", r4)
    r3.add_grabbables("book")
    r3.add_item("bookshelves", "Empty with no books.")
    r3.add_item("statue", "Nothing special about it.")
    r3.add_item("desk", "A statue rests on the desk, along with a book.")

    # create room 4
    r4.add_exit("north", r2)
    r4.add_exit("west", r3)
    r4.add_exit("south", None)
    r4.add_grabbables("6-pack")
    r4.add_item("brew_rig", "Someone was brewing some sort of delicious beverage. A 6-pack rests next to it.")

    # set the current room
    current_room = r1


def death():
    # there is a better version in the pdf if you'd like it lol #we haven't the time - tj
    print("You got dead.")


# START THE GAMEEEEEEEE
inventory = []
create_rooms()

# game loop (play forever until the player dies or asks to quit)
while (True):
    status = "{}\nYou are carrying: {}\n".format(current_room, inventory)

    # if the current room is None, the player is dead
    if (current_room == None):
        death()
        break

    # display status
    print("==========================")
    print(status)

    # prompt for player input
    # game supports a simple language of <verb> <noun>
    # valid verbs are go, look, and take
    # valid nouns depend on the verb
    action = input("What to do? ")
    action = action.lower()

    # exit the game if the player types 'quit', 'exit', or 'bye'
    if (action == "quit" or action == "exit" or action == "bye"):
        break

    # set a default response
    response = "I don't understand. Try <verb> <noun>. Valid verbs are go, look, and take."

    # split the user input into words and store the words in a list
    words = action.split()

    # the game only understands two workd inputs
    if (len(words) == 2):
        verb = words[0]
        noun = words[1]

        # the verb is: go
        if (verb == "go"):
            # set a default response
            response = "invalid exit."

            # check for valid exits in the current room
            for i in range(len(current_room.exits)):
                # a valid exit is found
                if (noun == current_room.exits[i]):
                    # change the current room
                    current_room = current_room.exit_locations[i]
                    # set the response
                    response = "room changed."
                    # no need to check anymore exits
                    break

        # the verb is: look
        if (verb == "look"):
            # set a default response
            response = "I don't see that item."

            # check for valid items in the current room
            for i in range(len(current_room.items)):
                # a valid item is found
                if (noun == current_room.items[i]):
                    # set the response to the item's description
                    response = current_room.item_descriptions[i]
                    break

        # the verb is: take
        if (verb == "take"):
            # set a default response
            response = "I don't see that item."

            # check for valid grabbable items in the current room
            for grabbable in current_room.grabbables:
                # a valid grabbable item is found
                if (noun == grabbable):
                    # add the grabbable item to player's inventory
                    inventory.append(grabbable)
                    # remove the grabbable item from the room
                    current_room.del_grabbable(grabbable)
                    # set the response
                    response = "Item grabbed."
                    break

    # display the response
    print("\n{}".format(response))

    # START PLANNING OUT IMPROVEMENTS WE WANT TO MAKE AND HOW TO DO THAT
    # PROJECT DUE JANUARY 11TH!!!!!!!!

    # take key off table description when key is grabbed
    # make the game make sense
