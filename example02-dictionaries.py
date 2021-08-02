#!/usr/bin/python3


def main():
    # create empty dictionary
    webster = {}


    # create a 3 dict with several entries
    elf = {'str': 4, 'dex': 9, 'int': 7}
    human = {'str': 6, 'dex': 5, 'int': 5}

    troll = {'str': 9, 'dex': 2, 'int': 2}


    # display the str of elf
    print(elf['str'])
    # print(elf['arrows']) # this would cause an error that stopped the program!
    print(elf.get('arrows')) # .get() is a dict method it returns "None" by default
    print(elf.get('arrows', None)) # this line is the SAME as the one above (None is the default)
    print(elf.get('arrows', 'That is not a valid character stat!'))

    # display the dex of troll
    print(troll.get('dex'))

    # create a player dict
    player = {'str': 5, 'dex': 7, 'int': 7, 'inventory': []}

    # display the dictionary named player
    print(player)

    # show the player inventory
    print(player.get('inventory'))

    # the player found a gold harp
    player.get('inventory').append('gold harp')

    # the player found a dagger
    player['inventory'].append('dagger')  # generally this method of accessing a dict is less desirable
                                          # it will cause an ERROR if the key in the "dict[key]" is not found
    # show the player inventory
    print(player.get('inventory'))

    # display the dictionary named player
    print(player)

if __name__ == "__main__":
    main()
