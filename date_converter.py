import unittest
from datetime import datetime, timedelta


def convert_datetime(date: str, format_from: str = '%Y-%m-%dT%H:%M:%S', format_to: str = '%H:%M - %d.%m.%y'):
    """Переконвертация строки времени"""
    date = date.replace(' ', '')
    print(date)
    try:
        result = datetime.strptime(date, format_from)
    except ValueError:
        datetime.strptime(date, format_from) - timedelta(days=1)
    return datetime.strptime(date, format_from) - timedelta(days=1)


class TestConvert(unittest.TestCase):

    def test_move_zeros(self):
        """"""

        self.assertEqual(convert_datetime(' 11:43  - 29.02.22', '%H:%M-%d.%m.%y', '%H:%M - %d.%m.%y'), '11:43 - 28.02.22')
        # self.assertEqual(convert_datetime('11:43 - 30.02.22'), '11:43 - 30.02.22')
        # self.assertEqual(convert_datetime('11:43 - 30.02.22'), '11:43 - 30.02.22')
        # self.assertEqual(convert_datetime('11:43 - 30.02.22'), '11:43 - 30.02.22')
        # self.assertEqual(convert_datetime('11:43 - 30.02.22'), '11:43 - 30.02.22')


# python -m unittest -v convert_datetime.py
