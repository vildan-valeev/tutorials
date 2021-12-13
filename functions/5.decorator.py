def decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Код до выполнения функции')
        result = func()
        print('Код, который сработал после функции')
        return result

    return wrapper


@decorator
def show():
    print("Я обычная функция")


show()


#  - args, kwargs
def decorator_2(func):
    def wrapper(*args, **kwargs):
        print(f'ТРАССИРОВКА: вызвана {func.__name__}() '
              f'c {args}, {kwargs}')

        result = func(*args, **kwargs)

        print(f'ТРАССИРОВКА: {func.__name__}() '
              f'вернула {result}')
        return result

    return wrapper


@decorator_2
def show_2(name):
    print(f"{name}, Я обычная функция")


show_2('Вася')


# перенос строки документации и других метаданных
import functools
def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func.upper()
    return wrapper