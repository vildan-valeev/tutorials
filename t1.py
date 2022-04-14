# import datetime as dt
# в данном случае предпочтительнее импортировать "конкретный" модуль - datetime
# чтобы избегать путаницы в datetime.datetime и ограничения по длине строк
from datetime import datetime as dt


# TODO: аннотации типов
# TODO: docstrings

class Record:
    #  docstrings
    """ """

    def __init__(self, amount, comment, date=''):
        self.amount = amount
        # так более лаконично, но можно лучше)
        self.date = (dt.now().date() if not date
                     else dt.strptime(date, '%d.%m.%Y').date())
        # self.date = (
        #     dt.datetime.now().date() if
        #     not
        #     date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    #  docstrings
    """ """

    def __init__(self, limit):
        self.limit = limit
        self.records = []
        # self.records: List[Record] = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        #  docstrings
        """ """
        today_stats = 0
        # для переменной цикла нежелательно использовать название класса
        # лучше указать в typing,
        # если необходимо видеть атрибуты и методы в ide
        for record in self.records:
            if record.date == dt.now().date():
                today_stats += record.amount
                # укороченная запись
                # today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self):
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
    #  docstrings
    """ """

    def get_calories_remained(self):
        #  docstrings
        """ Получает остаток калорий на сегодня """
        x = self.limit - self.get_today_stats()
        if x > 0:
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        # else:
        #     return ('Хватит есть!')
        # лишний else,
        # если return попадает в if то исполнение кода дальше не идет,
        # т.е. мы "отлавливаем" только if-ы, все остальное это основной return
        return 'Хватит есть!'


class CashCalculator(Calculator):
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.
    RUB_RATE = float(1)  # Курс Рубля.

    def get_today_cash_remained(self, currency):
        #  docstrings
        """ """
        # USD_RATE, EURO_RATE не нужны, внутри вызываем как self.USD_RATE

        # Путаница в переменных, Переменные со словом type нежелательны.
        # Это не тип, это строка

        cash_remained = self.limit - self.get_today_stats()

        # создание пустой переменной на случай если не будет выполнено
        # какое-либо условие
        suffix = ''
        # TODO: три if с одинаковой логикой....
        if currency == 'usd':
            cash_remained /= self.USD_RATE
            suffix = 'USD'
        elif currency == 'eur':
            cash_remained /= self.EURO_RATE
            suffix = 'Euro'
        elif currency == 'rub':
            # можно стандартизировать логику cash_remained
            cash_remained /= self.RUB_RATE
            suffix = 'руб'
        # "грядка" elif-ов не всегда нужна, если условия небольшие достаточно
        # тернарным оператором
        if cash_remained > 0:
            return f'На сегодня осталось {round(cash_remained, 2)} {suffix}'
        answer = 'Денег нет, держись '
        return (answer if cash_remained == 0
                else answer + f'твой долг {cash_remained:.02f} {suffix}')

    def get_week_stats(self):
        #  docstrings
        """ """
        super().get_week_stats()

# если *.py исполняющий, то требуется конструкция "main"
