# import datetime as dt
# в данном случае предпочтительнее импортировать "конкретный" модуль - datetime
# чтобы избегать путаницы в datetime.datetime и ограничения по длине строк
from datetime import datetime as dt
from typing import List


# необходимо изначально определиться с какими типами (float, int и тд) работает
# клиент, и с какими типами будет работать программа
# т.к. могут быть ошибки непредвиденные.


class Record:
    #  docstrings
    """ """
    def __init__(self, amount: int, comment: str, date: str = ''):
        self.amount = float(amount)
        self.date = dt.now().date() if not date \
            else dt.strptime(date, '%d.%m.%Y').date()
        self.comment = comment


class Calculator:
    #  docstrings
    """ """
    def __init__(self, limit: float):
        self.limit = limit
        # self.records = []
        self.records: List[Record] = []

    def add_record(self, record) -> None:
        #  docstrings
        """ """
        self.records.append(record)

    def get_today_stats(self) -> int:
        #  docstrings
        """ """
        today_stats = 0
        # for Record in self.records:
        # для переменной цикла нежелательно использовать название класса
        # лучше указать в typing
        for record in self.records:
            if record.date == dt.now().date():
                today_stats += record.amount
                # укороченная запись
                # today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self) -> int:
        #  docstrings
        """ """
        week_stats = 0
        today = dt.now().date()
        for record in self.records:
            # if (
            #         (today - record.date).days < 7 and
            #         (today - record.date).days >= 0
            # ):
            # можно объединить два условия, скобки не требуются
            if 7 > (today - record.date).days >= 0:
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        #  docstrings
        """ Получает остаток калорий на сегодня """
        x = self.limit - self.get_today_stats()
        if x > 0:
            # return f'Сегодня можно съесть что-нибудь
            # f не нужен если нет работы с переменными
            return 'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        # else:
        #     return ('Хватит есть!')
        # лишний else,
        # если return попадает в if то исполнение кода дальше не идет,
        # т.е. мы "отлавливаем" только if-ы, все остальное это основной return
        return 'Хватит есть!'


class CashCalculator(Calculator):
    # можно заранее создать структуру данных
    RATE = {
        'usd': (float(60), 'USD', 'USD_RATE'),  # Курс доллар США.
        'eur': (float(70), 'Euro', 'EURO_RATE'),  # Курс Евро.
        'rub': (float(1), 'руб', 'RUB_RATE')
    }

    # TODO: если будет в класс передаваться кастомный USD_RATE
    #  (по условию он не нужен), то необходимо дополнить функционал

    def __ge_currency(self, rate):
        #  docstrings
        """ """
        cash_remained = self.limit - self.get_today_stats()
        return cash_remained / self.RATE[rate][0], self.RATE[rate][1]

    def get_today_cash_remained(self, currency):
        #  docstrings
        """ """
        # определение курса волют лучше задавать в отдельном методе
        # каждый метод должен выполнять только свою логику,
        # с минимальными "перекрестными" условиями(так легче тестировать)

        # currency_type = currency
        # cash_remained = self.limit - self.get_today_stats()
        # if currency == 'usd':
        #     cash_remained /= USD_RATE
        #     currency_type = 'USD'
        # elif currency_type == 'eur':
        #     cash_remained /= EURO_RATE
        #     currency_type = 'Euro'
        # elif currency_type == 'rub':
        #     cash_remained == 1.00
        #     currency_type = 'руб'
        # Переменные со словом type не использовать. Это не тип, это строка
        cash_remained, suffix = self.__ge_currency(currency)
        if cash_remained > 0:
            return f'На сегодня осталось {cash_remained:.02f)} {suffix}'
            # return (
            #     f'На сегодня осталось {round(cash_remained, 2)} '
            #     # форматирование float в f строках можно задавать так
            #     # f'На сегодня осталось {cash_remained:.2f)} {currency_type}'
            # )
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            # в python3 более идеальным вариантом считается без использования
            # метода format
            return 'Денег нет, держись: ' \
                   f'твой долг - {-cash_remained:.02f} {suffix}'

    def get_week_stats(self):
        #  docstrings
        """ """
        super().get_week_stats()


# если *.py исполняющий, то требуется конструкция "main"
if __name__ == '__main__':
    cash_calculator = CashCalculator(1000)

    # cash_calculator.add_record(Record(amount=145, comment="кофе"))
    cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
    cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
    cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
    print(cash_calculator.get_today_stats())
    print(cash_calculator.get_today_cash_remained("rub"))
    # cash_calculator = CashCalculator(1000)
    #
    #
    # cash_calculator.add_record(Record(amount=145, comment="кофе"))
    # cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
    # cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
    # cash_calculator.add_record(
    #     Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
    # print(cash_calculator.get_today_cash_remained("rub"))
