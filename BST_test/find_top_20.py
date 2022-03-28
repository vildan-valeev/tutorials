import logging
import unittest
from typing import List

"""
Подходило 1 сентября, университет готовился к наплыву абитуриентов. Так вышло, что Вы, как программист, 
должны были помочь в отборе тех абитуриентов, кто поступит в университет на конкурсной основе 
на специальность программиста. 

Схема была проста: есть абитуриент, у него есть результаты сданных экзаменов по математике, русскому и информатике. 
Соответственно, у каждого потенциального студента есть сумма баллов по этим экзаменам. 
Также есть дополнительные (extra_scores) баллы: за волонтерство, участие в олимпиадах и другие активности. 

Вам нужно отобрать 20 человек, у которых суммарный балл выше, чем у других. В случае, если не получается 
однозначно определить 20 человек (например, 2 человека набрали одинаковое СУММАРНОЕ количество баллов и 
претендуют на 20 место в списке, стоит их ранжировать по "профильным" дисциплинам - "информатике" и "математике").
"""


class FindTop:  # -> List[dict]
    """ТОП-20: сортировка"""

    def __init__(self, candidates: List[dict], top: int = 20):
        self.top = top
        self.candidates = candidates

    @staticmethod
    def full_score(i: dict) -> int:
        """сумма всех баллов"""
        return i['scores']['math'] + i['scores']['russian_language'] + i['scores']['computer_science'] + i[
            'extra_scores']

    @staticmethod
    def last_chance(i: dict) -> int:
        """баллы информатика и математика"""
        return i['scores']['math'] + i['scores']['computer_science']

    def check(self):
        """проверка валидация и прочее"""
        if len(self.candidates) < self.top:
            logging.info('не хватает кандидатов')
            return
            # raise ValueError()
        return True

    def sort_top(self, ) -> List[dict]:
        """Cортировка (пузырьком)"""
        if not self.check():
            return []
        for i in range(len(self.candidates) - 1):
            for j in range(len(self.candidates) - i - 1):
                c_full_curr = self.full_score(self.candidates[j])
                c_full_next = self.full_score(self.candidates[j + 1])
                if c_full_curr > c_full_next:
                    self.candidates[j], self.candidates[j + 1] = self.candidates[j + 1], self.candidates[j]
                elif c_full_curr == c_full_next:
                    if self.last_chance(self.candidates[j]) > self.last_chance(self.candidates[j + 1]):
                        self.candidates[j], self.candidates[j + 1] = self.candidates[j + 1], self.candidates[j]
        return self.candidates[::-1][:self.top]


class TestFind(unittest.TestCase):

    def setUp(self) -> None:
        self.candidates = [
            {"name": "V", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
            {"name": "V2", "scores": {"math": 60, "russian_language": 60, "computer_science": 48}, "extra_scores": 0},
            {"name": "P2", "scores": {"math": 92, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
            {"name": "P", "scores": {"math": 92, "russian_language": 35, "computer_science": 32}, "extra_scores": 1},
            {"name": "F", "scores": {"math": 53, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
            {"name": "F2", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},

        ]
        self.answer = [
            {"name": "F", "scores": {"math": 53, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
            {"name": "V2", "scores": {"math": 60, "russian_language": 60, "computer_science": 48}, "extra_scores": 0},
            {"name": "V", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
            {"name": "F2", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
            {"name": "P2", "scores": {"math": 92, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
        ]

    def test_find_top_20(self):
        """"""
        instance = FindTop(self.candidates, 5)
        self.assertEqual(instance.sort_top(), self.answer)

# python -m unittest -v find_top_20.py
