# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    
    def __init__(self, name, description, inventory=[]):
        self.name = name
        self.description = description
        self.inventory = inventory

    def __repr__(self):
        # output = "You find yourself " + self.name + ". " + self.description + "."
        # for i in self.inventory:
        #     output += "\n" + str(i)

        # return output
        return "You find yourself " + self.name + ". " + self.description + "."

