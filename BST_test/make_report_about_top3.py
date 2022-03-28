"""
У студентов-программистов шел последний год обучения, и близилась выдача дипломов.
К этой знаменательной дате было решено подготовить символические подарки трем студентам, которые имеют максимальный
средний балл по итогам обучения. Но задача осложнялась тем, что нужно предоставить эти данные в бухгалтерию, причем так,
чтобы главный бухгалтер Ольга Петровна, списывающая деньги на подарки, смогла открыть это в своём любимом Excel.

Впрочем, для Вас, человека, который работает не первый год в данном учреждении, это не казалось невыполнимой задачей.

Функция make_report_about_top3 принимает словарь (students_avg_scores), в котором ключами являются имена студентов,
а значениями — средний балл за всю учебу. Функция находит ТОП-3 студентов, чей средний балл выше, чем у других.
Функция возвращает ссылку на эксель-файл, в котором упомянуты 3 студента и который потом будет передан в бухгалтерию.
Сам файл необходимо создать внутри функции. Важно сохранить совместимость с Excel, чтобы Ольга Петровна смогла без
проблем получить всю нужную информацию. Пример входных данных приведен ниже
"""
import pathlib
import unittest
import csv


def make_report_about_top3(students: dict) -> pathlib.Path.absolute:
    """ save top-3"""
    file_name = 'output.xlsx'
    with open(file_name, 'w+') as output:
        writer = csv.writer(output)
        for key, value in dict(sorted(students.items(), key=lambda item: item[1], reverse=True)[:3]).items():
            writer.writerow([key, value])
    return pathlib.Path.cwd() / file_name


class TestMakeReport(unittest.TestCase):

    def setUp(self) -> None:
        self.scores = {
            'Max': 4.964,
            'Eric': 4.962,
            'Peter': 4.923,
            'Mark': 4.957,
            'Julie': 4.95,
            'Jimmy': 4.973,
            'Felix': 4.937,
            'Vasya': 4.911,
            'Don': 4.936,
            'Zoi': 4.937
        }

    def test_find_top_20(self):
        """"""
        path = pathlib.Path.cwd() / 'output.xlsx'
        self.assertEqual(make_report_about_top3(self.scores), path)

# python -m unittest -v make_report_about_top3.py
