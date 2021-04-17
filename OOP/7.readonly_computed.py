
# Только на чтение
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


# Вычисляемые значения и кеширование вычисляемых значений
class Person:

    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._full_name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._full_name = None

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value
        self._full_name = None

    @property
    def full_name(self):
        if self._full_name is None:
            self._full_name = f'{self._surname} {self._name}'
        return self._full_name
