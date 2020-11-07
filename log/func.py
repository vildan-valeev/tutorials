import logging

# logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
#                     level=logging.INFO,)
log = logging.getLogger(__name__)

def test(a):
    """print(__doc__)"""
    log.info('Cтарт функции')
    return a ** 2