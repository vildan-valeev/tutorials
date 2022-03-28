"""
Шел 2021 год. Большая часть студентов, которых Вы когда-то помогли отобрать для поступления в университет,
успешно учится. В знак благодарности вам выделили личный кабинет, поскольку помощь оказалась неоценимой.
Отношения с коллегами стали крепче после тех дней. Кстати, о коллегах…

Однажды утром возле двери кабинета Вы встретились с зам. декана, который выглядел озадаченно. После недолго объяснения
стало понятно, что местный военкомат интресуется, сколько студентов мужского пола являются военнообязанными
достигшими 18 лет). Нужно сформировать список этих студентов.

В качестве исходных данных вам предлагают лист, на котором написаны имена студентов, их пол и возраст. К несчастью,
где-то по центру этого листа расположено огромное пятно от пролитого кофе, что испортило часть записей. Единственное,
что осталось нетронутым — имена.

Функция get_inductees принимает 3 списка одинаковой длины. В первом списке (names) — имена студентов, позволяющие их
точно идентифицировать. Во втором (birthday_years) — год рождения. В третьем (genders) — пол студента.Частично они
отсутствуют ввиду испорченного листа бумаги. Функция возвращает список с именами студентов мужского пола, которые
достигли или могут достигнуть 18 лет в 2021 году, но при этом не старше 30 лет. Cтуденты, по которым невозможно
точно установить - попадают они в список или нет (из-за порчи данных), должны быть выведены отдельно. Пример входных
данных приведен ниже

"""
import unittest
from typing import List, Optional, Tuple

names = ["Vasya", "Alice", "Petya", "Jenny", "Fedya", "Viola", "Mark", "Chris", "Margo"]
birthday_years = [1992, 1995, 2000, None, None, None, None, 1998, 2001]
genders = ["Male", "Female", "Male", "Female", "Male", None, None, None, None]


def get_inductees(names_: List[str], birthday_years_: List[Optional[int]], genders_: List[Optional[str]]) -> Tuple[
    List[str], List[str]]:
    """Собираем военнообязанных в армию - за ордууууууу))))"""

    female = 'Female'
    # приводим к list of dict для сортировки (отсортирован по non-female)
    students = [{'name': n, 'b_year': b, 'gen': g} for n, b, g in zip(names_, birthday_years_, genders_) if g != female]
    inductees = []
    unidentified = []
    other = []
    # import datetime  # move to top
    # year_now = datetime.datetime.now().year  # для 2022 года
    for i in students:
        if i['b_year'] is None:  # без даты рождения всех в unidentified
            unidentified.append(i['name'])
        # elif 18 <= year_now - i['b_year'] < 30:
        elif 18 <= 2021 - i['b_year'] < 30:
            if i['gen'] is not None:  # кто от 18 и до 30 с гендером Male - в inductees,
                inductees.append(i['name'])
            else:  # остальные в unidentified - без гендера но подходят по дате
                unidentified.append(i['name'])
        else:  # все остальные - c датой и Male, но не подходят по возрасту
            other.append(i['name'])
    return inductees, unidentified


class TestInductees(unittest.TestCase):
    def setUp(self) -> None:
        self.names = ["Vasya", "Alice", "Petya", "Jenny", "Fedya", "Viola", "Mark", "Chris", "Margo"]
        self.birthday_years = [1992, 1995, 2000, None, None, None, None, 1998, 2001]
        self.genders = ["Male", "Female", "Male", "Female", "Male", None, None, None, None]
        self.answer = (['Vasya', 'Petya'], ['Fedya', 'Viola', 'Mark', 'Chris', 'Margo'])

    def test_get_inductees(self):
        """"""
        self.assertEqual(get_inductees(self.names, self.birthday_years, self.genders), self.answer)

# python -m unittest -v get_inductees.py
