import unittest


# SQL =

# SELECT name, transaction.amount
# FROM transaction
# INNER JOIN account
# ON account.id = transaction.account_id
# WHERE DATE(transaction.created) = DATE('now')
# ORDER BY transaction.amount DESC
# LIMIT 5;


def is_float(amount):
    """Проверка может ли str быть float"""
    try:
        float(amount)
        return True
    except ValueError:
        # print('to log: must be float as tr')
        return False


class Account:
    def __init__(self, balance: str = '0', ):
        if not self.check(balance):
            raise ValueError("ValueError exception")
        self.balance = float(balance)

    def check(self, amount):
        """Validate"""
        if is_float(amount):
            tmp = float(amount) * 100  # проверка на остаток: -100.005 -> -10000.5,  и если 0 т.е. 10.0 isint
            return True if tmp.is_integer() and tmp > 0 else False
        return False

    def add_to_balance(self, amount: str) -> float:
        """Увеличиваем баланс"""
        if self.check(amount):
            self.balance += float(amount)
        return self.balance

    def minus_balance(self, amount: str):
        """уменьшаем баланс, если недостаточно то списываем что остаток"""
        if self.check(amount):
            temp_balance = self.balance
            if self.balance <= float(amount):
                self.balance = 0
                return temp_balance
            self.balance -= float(amount)
            return self.balance


#
class TestAccount(unittest.TestCase):

    def setUp(self):
        self.wrong_init = ['-100', '100z', '-2020.0054.sdf']
        self.amount_list = [('', False), ('-100z', False), ('200.00', True), ('200.001', False), ('100', True),
                            ('2000000.15', True)]
        self.account = Account('10')

    def test_check_amount(self):
        """"""
        for k, v in self.amount_list:
            self.assertEqual(self.account.check(k), v)

    def test_add_to_balance(self):
        self.account.add_to_balance('40')
        self.assertEqual(self.account.balance, 50)

    def test_minus_from_balance(self):
        self.account.minus_balance('50')
        self.assertEqual(self.account.balance, 0)
        self.account.add_to_balance('18')
        self.account.minus_balance('5')
        self.assertEqual(self.account.balance, 13)

    def test_init_account(self):

        for i in self.wrong_init:
            with self.assertRaises(ValueError):
                Account(i)

# python -m unittest -v elm_soft.py
