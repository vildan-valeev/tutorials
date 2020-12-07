from typing import Protocol, List


class Bird:
    def fly(self):
        print('fly whith wings')

class AirPlane:
    def fly(self):
        print('fly with fuel')


class Flyable(Protocol):
    def fly(self): ...


def process_flyables(flyables: List[Flyable]):
    for cur_obj in flyables:
        cur_obj.fly()


class Fish:
    def swim(self):
        print('swim in water')


process_flyables([Bird(), AirPlane(), Fish()])
