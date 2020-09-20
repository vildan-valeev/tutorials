method = 'auth.check'
code_response = 200


class Service:
    def __init__(self, request):
        self.request = request


    def check(self):
        if self.request =



############################
s = Service


@s.check
def main(request):
    print("Ок, добро )))")


if __name__ == '__main__':
    main('пароль')






########################################

# def decorator_function(func):
#     def wrapper():
#         print('Функция-обёртка!')
#         print('Оборачиваемая функция: {}'.format(func))
#         print('Выполняем обёрнутую функцию...')
#         func()
#         print('Выходим из обёртки')
#
#     return wrapper
#
#
# @decorator_function
# def hello_world():
#     print('Hello world!')
#

