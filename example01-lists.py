#!/usr/bin/python3

def main():

    pcGames = ['Tetris', 'Minecraft', 'Starcraft']

    nintendoGames = ['Mario Brothers', 'Animal Crossing', 'Zelda']



    # I want to track my video games in a single list
    games = []
    # If I want to add ALL the games to a single list...
    games.extend(pcGames)
    games.extend(nintendoGames)
    print("Now all of my games are in a single list, 'games'")
    print(games)
    print(games[0])


    # make it easier to read
    print()


    # If I want to have a single list of lists...
    orderedgames = []
    orderedgames.append(pcGames)
    orderedgames.append(nintendoGames)
    print("Now I have a single list that contains all of my sub list data...")
    print(orderedgames)
    print(orderedgames[0])
    print(orderedgames[0][0])


if __name__ == "__main__":
    main()
