from pprint import pprint
from functools import wraps
from enum import Enum, unique
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
    Decorator that adds a header before the function print out
    '''
    @wraps(funct)
    def add_header(*args, **kwargs):
        LENGTGH = 60
        print('\n' + '-' * LENGTGH)
        print(funct.__name__.center(LENGTGH))
        print('-' * LENGTGH)
        funct(*args, **kwargs)
        print()
    return add_header


@heading
@timethis
def myDict():
    '''
    Example for using dictionaries
    '''
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
def myDataTypes():
    '''
    Example or the data types in python
    '''
    # array
    my_list = ['abcd', 786, 2.23, 'john', 70.2]    # elements can be added
    print('List: ', my_list)
    print('List: ', my_list[2:])
    print('List: ', my_list[1:3])
    my_list.append('Heros')
    print('List: ', my_list)
    print()

    # same like list but you can add or change elements
    my_tupel = ('abcd', 786, 2.23, 'john', 70.2)    # no elements can be added
    print('Tupel: ', my_tupel)
    print('Tupel: ', my_tupel[2:])
    print('Tupel: ', my_tupel[1:3])
    # my_tupel.append('frieda')     # <- this will cause an error
    # my_tupel[0] = 'abcdefg'       # <- this will cause an error
    print()

    # dictionary
    my_dict = {'1': 'Otto', 2: 'Heinz', 'pi': 3.414}
    print('Dict: ', my_dict)
    print('Dict: ', my_dict[2])
    print('Dict: ', my_dict['pi'])
    print()

    # a set contains unique and immutable elements
    my_set = {'Hamburg', 'München', 'Frankfurt', 'Berlin'}
    print(my_set)
    my_set.add('Lingen')
    print(my_set)
    # my_set.add(['Singen', 'Böhringen'])     # <- this will cause an error
    my_frozenset = frozenset(my_set)
    print(my_frozenset)
    # my_frozenset.add('Radolfzell')      # <- this will cause an error


@heading
def myLogging():
    '''
    Example for logging
    '''
    logging.basicConfig(format='%(asctime)s %(levelname)s %(funcName)s[%(lineno)d] - %(message)s', level=logging.DEBUG)  # nopep8
    logging.warning('This is a warning')
    logging.debug('This is a debug message')
    logging.fatal('This is a fatal message')
    logging.error('This is an error message')


# @unique
class Colors(Enum):
    '''
    class Enum
    Having two enum members with the same name will cause an error.
    But two enum members are allowed to have the same value. This kind of alias
    '''
    RED = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4.346
    PINK = 4        # <- OK, if no decorator @unique. This is an alias
    # YELLOW = 5    # <- his will causes an error


@heading
def myEnum():
    '''
    Example for Enums
    '''
    print('Colors: ', list(Colors))
    print('Interrate through Colors: ')
    for color in Colors:
        print(color.name, ' has the value ', color.value)
    print(Colors.PINK)
    print(Colors.YELLOW)


@heading
def myMap():
    '''
    Example for maps
    '''
    # map iterator can only b used once!!!
    my_map = map(lambda x: x * x, range(1, 11))
    print(list(my_map))

    # you can use more then one list
    my_map = map(lambda x, y: x + y, range(1, 11), range(100, 111))
    print(list(my_map))


@heading
def myFilter():
    '''
    Example for filter
    '''
    # filter
    even_numbers = list(filter(lambda x: not(x % 2), range(1, 51)))
    print(even_numbers)

    odd_numbers = list(filter(lambda x: x % 2, range(1, 51)))
    print(odd_numbers)


class Const(object):
    '''
    Example for constants. Constants are not xisting in python
    '''

    def __init__(self):
        self.__timeout = 10000
        self.__header = 'This is the header'
        self.__pi = 3.414

    @property
    def TIMEOUT(self):
        return self.__timeout

    @property
    def HEADER(self):
        return self.__header

    @property
    def PI(self):
        return self.__pi


@heading
def myConst():
    const = Const()
    print(const.PI)
    print(const.HEADER)
    print(const.TIMEOUT)
    try:
        const.TIMEOUT = 1       # <- you cant set attribute (no eter defined)
    except AttributeError:
        print('ups - AttributeError -> You cant set the atribute, because no setter is defined')
    print('hihihi')


if __name__ == '__main__':
    myDict()
    myLogging()
    myEnum()
    myDataTypes()
    myMap()
    myFilter()
    myConst()
