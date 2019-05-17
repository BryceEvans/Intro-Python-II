from room import Room

class Item(Room):

    def __init__(self, name, description, value):
        # super().__init__(name, description)
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "\n" + self.name + " is available for pickup. And is worth " + self.value + " coins. It is described as: " + self.description + "." 