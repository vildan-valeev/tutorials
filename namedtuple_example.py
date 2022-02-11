from collections import namedtuple

Player = namedtuple('Player', 'name age rating')

players = [Player('Carlsen', 1990, 2842), Player('Caruana', 1992, 2822), Player('Mamedyarov', 1985, 2801)]

print(players[0])

print(players[0].name)