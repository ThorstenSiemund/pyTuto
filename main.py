from pprint import pprint
from functools import wraps
import logging
import time


def timethis(func):
    '''
    Decorator that reports the execution time in seconds.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, ': ', end - start, 'seconds')
        return result
    return wrapper


def heading(funct):
    '''
    Decorator that adds a header before the function call
    '''
    @wraps(funct)
    def add_header(*args, **kwargs):
        print(funct.__name__.center(40))
        print('-' * 40)
        funct(*args, **kwargs)
        print()
    return add_header


@heading
@timethis
def myDict():
    # print('myDict'.center(30))
    # print('-' * 30)
    keys = 'Thorsten Heike Hanna Frieda Otto Heinz'.split()
    value1 = 'blau rot gelb orange schwarz weiss'.split()
    value2 = 'Apfel Karotte Paprika Zwiebel Rotkohl Birne'.split()
    print('Keys: ', keys)
    print('Values1: ', value1)
    print('Values2: ', value2)
    my_dict = dict(zip(keys, zip(value1, value2)))
    pprint(my_dict)
    # pprint(my_dict['Thorsten'])
    # print('Values of "Thorsten": ', my_dict['Thorsten'])


@heading
def myLogging():
    logging.basicConfig(format='%(asctime)s %(levelname)s %(funcName)s[%(lineno)d] - %(message)s', level=logging.DEBUG)  # nopep8
    logging.warning('This is a warning')
    logging.debug('This is a debug message')
    logging.fatal('This is a fatal message')
    logging.error('This is an error message')


@heading
def myEnums():
    names = 'Thorsten Heike Hanna Frieda Otto Heinz'.split()
    print(list(enumerate(names)))
    print(list(enumerate(names, start=11)))


@heading
def main():
    pass


if __name__ == '__main__':
    myDict()
    myLogging()
    myEnums()