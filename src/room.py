# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    
    def __init__(self, name, description, inventory=[]):
        self.name = name
        self.description = description
        self.inventory = ["dog"]

    def __repr__(self):
        return "You find yourself " + self.name + ". " + self.description + "."
        # return "The " + self.name + " is described is as follows: " + self.cur_room.description + "."
