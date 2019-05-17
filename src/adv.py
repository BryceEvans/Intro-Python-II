from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
"North of you, the cave mount beckons", [Item("Excalibur", """The sword fo excalibur""", 20)]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    'sword': Item("Excalibur", """The sword fo excalibur""", 20),
    'Shield': Item("Chest Shield", """Body armor for protection""", 15)
}

item['sword']

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
options = {
    "n": "North",
    "e": "East",
    "s": "South",
    "w": "West",
    "q": "Quit"
}

# Make a new player object that is currently in the 'outside' room.

player_one = Player("Player One", room["outside"])
direction = ""

# print(player_one)

while direction != 'q':
    moveOptions = ""
    print(player_one.cur_room)
    print(player_one.cur_room.inventory)
    for opt in options:
        moveOptions = options[opt], opt
        print(opt)
    
    while direction != 'q':
        direction = input("\n Chose a direction (n, e, s, w) to move: ")
        if hasattr(player_one.cur_room, f'{direction}_to'):
            # print(f'move options{direction}')
            # print("TRUE")
            if direction == 'n':
                player_one.cur_room = player_one.cur_room.n_to
                print("\n You are in " + str(player_one.cur_room))
            if direction == 'e':
                player_one.cur_room = player_one.cur_room.e_to
                print("\n You are in " + str(player_one.cur_room))
            if direction == 's':
                player_one.cur_room = player_one.cur_room.s_to
                print("\n You are in " + str(player_one.cur_room))
            if direction == 'w':
                player_one.cur_room = player_one.cur_room.w_to
                print("\n You are in " + str(player_one.cur_room))
        elif direction == 'q':
            print("\n Game Over!")
        else:
            print("\n Not a valid command.")


# Write a loop that:
#
# * Prints the current room name
#  --> look up room in dictionary...?
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# direction = input("Ender a direction (n,e,s,w) or q to quit.")
# If the user enters a cardinal direction, attempt to move to the room there.
# If user enters 'q', wite the game.

    # did user enter a valid direction?
    # Yes? - move in that direction, print new room info
    # Is there anything in that direction?
        # Yes ? -move in that direction, print new room info
        # No ? - print out message stating nothing in the direction
    # No ? - Print an error message if the movement isn't allowed.
    # continue prompting for input

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.