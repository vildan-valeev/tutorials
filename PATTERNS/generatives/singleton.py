"""
Singleton

В системе должен существовать только один экземпляр класса,
доступ к которому легко получить из любой точки клиентского кода

Достоинства:
1. Позволяет с любой точки клиентского кода обратиться к единственному экземпляру класса
2. Создание экземпляра осуществляется по принципу отложенной инициализации
3.
Недостатки
1. Бездумное использование паттерна может привести к плохому дизайну архитектуры
2. 
"""


class SingletonBaseClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonBaseClass, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MySingleton(metaclass=SingletonBaseClass):
    def __init__(self):
        self.name = 'Singleton'
        self.value_a = 3
        self.value_b = 5

    def add_a(self) -> int:
        return self.value_a + self.value_b

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name


from threading import Lock


class SingletonBaseClass(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


if __name__ == '__main__':
    my_singleton1 = MySingleton()
    my_singleton2 = MySingleton()
    print('Singletone1 name: ' + my_singleton1.get_name())
    my_singleton1.set_name('New Singleton')
    print('Singletone2 name: ' + my_singleton1.get_name())
    print(my_singleton1)
    print(my_singleton2)
    print(id(my_singleton1) == id(my_singleton2))
