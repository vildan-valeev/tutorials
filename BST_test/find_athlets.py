import unittest
from typing import List


def find_athlets(*args: List[str]) -> set:
    """ Определяем список совпадений.
        Количество совпадений имен в счетчике должна быть равна(или больше) количеству аргументов функции(списков)
        это будет значить что имя есть во всех списках.
    """
    return set.intersection(*[set(i) for i in args])


class TestFind(unittest.TestCase):

    def setUp(self) -> None:
        self.know_english = ["Vasya", "Jimmy", "Max", "Peter", "Eric", "Zoi", "Felix"]
        self.sportsmen = ["Don", "Peter", "Eric", "Jimmy", "Mark"]
        self.more_than_20_years = ["Peter", "Julie", "Jimmy", "Mark", "Max"]

    def test_find_athlets(self):
        """"""
        self.assertEqual(find_athlets(self.know_english, self.sportsmen, self.more_than_20_years), {'Peter', 'Jimmy'})

# python -m unittest -v find_athlets.py
