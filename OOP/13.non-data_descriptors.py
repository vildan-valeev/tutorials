from time import time
from random import choice


class Epoch:
    def __get__(self, instance, owner):
        return int(time())


class MyTime:
    epoch = Epoch()


m = MyTime()


# ----------------- было
# class Dice:
#     @property
#     def number(self):
#         return choice(range(1, 7))
#
#
# class Game:
#     @property
#     def rock_paper_scissors(self):
#         return choice(['Rock', 'Paper', 'Scissors'])
#
#     @property
#     def flip(self):
#         return choice(['Heads', 'Tails'])
#
#     @property
#     def number(self):
#         return choice(range(1, 7))


# g = Game()


# -------- стало
class Choice:
    def __init__(self, *choice):
        self._choice = choice

    def __get__(self, instance, owner):
        return choice(self._choice)


class Game:
    dice = Choice(1, 2, 3, 4, 5, 6, 7, )
    flip = Choice('Heads', 'Tails')
    rock_paper_scissors = Choice('Rock', 'Paper', 'Scissors')


g = Game()
