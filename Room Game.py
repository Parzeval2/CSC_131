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