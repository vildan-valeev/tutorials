import pytz
from datetime import datetime

WHITE = '\033[00m'
GREEN = '\033[0;92m'
RED = '\033[1;31m'


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self._history = []

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount: int):
        self.__balance += amount
        self.show_balance()
        self._history.append([amount, self._get_current_time()])

    def withdraw(self, amount: int):
        if self.__balance > amount:
            self.__balance -= amount
            print(f'You spend {amount} units')
            self.show_balance()
            self._history.append([-amount, self._get_current_time()])
        else:
            print('Not enough money')
            self.show_balance()

    def show_balance(self):
        print(f'Balance: {self.__balance}')

    def show_history(self):
        for amount, date in self._history:
            if amount > 0:
                transaction = 'deposited'
                color = GREEN
            else:
                transaction = 'withdrawn'
                color = RED
            print(f'{color} {amount} {WHITE} {transaction} on {date.astimezone()}')


# python -i 4.account.py

a = Account('oleg', 0)
