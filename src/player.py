# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, cur_room):
        self.name = name
        self.cur_room = cur_room
        # self.inventory = []

    # def __repr__(self):
    #     return self.name + ", you are in the " + self.cur_room + "."

    # def currentRoom(self):
    #     return self.cur_room

