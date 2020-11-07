import logging
from log.func import test


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,)


l = [1, 4, 3, 5, 2, 6, 8]

# def test(a):
#     """print(__doc__)"""
#     logging.info('Cтарт функции')
#     return a ** 2

result = 0

for i in l:

    result += test(i)
    logging.info(f'Предварительный результат {result}')

