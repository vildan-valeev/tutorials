import time


def decorator(func):
    def wrapper(*args, **kwargs):
        time1 = time.perf_counter()
        func(*args, **kwargs)
        time2 = time.perf_counter()
        print(f'Время выполнения функции {time2 - time1}')

    return wrapper


@decorator
def show(z):
    time.sleep(3)
    print(f"Я обычная функция - {z}")


show('cc')
