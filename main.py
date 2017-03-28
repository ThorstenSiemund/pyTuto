from mymodule import main_timeit
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
    LOG_FILENAME = 'logging_example.log'

    logging.basicConfig(format='%(asctime)s %(levelname)s %(funcName)s[%(lineno)d] - %(message)s',  # nopep8 E501
                        filename=LOG_FILENAME, level=logging.DEBUG)
    logging.warning('This is a warning')
    logging.debug('This is a debug message')
    logging.fatal('This is a fatal message')
    logging.error('This is an error message')

    # TODO: logging config by file
    # TODO: rotating file handler


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
        print('ups - AttributeError -> You cant set the attribute, because no setter is defined')   # nopep8 E501


@heading
def myStringFormatting():
    print('First argument: {0} - second argument: {1}'.format(47, 12))
    print('First argument: {0:03d} - second argument: {1:7.2f}'.format(47, 12))

    print('Precisions: {0:6.2f} - {0:6.8f}'.format(3.41481234))
    print('Precisions: {0:{width}}'.format(123, width=6))
    print('Values are: {0:+06d} {1:-06d}'.format(378, -378))
    print("The value is {:,}".format(12334567))

    print('{0:30s}'.format('This is a string'))
    print('{0:>30s}'.format('This is also a string'))

    print("\nThe capital of {province} is {capital}".format(province="Ontario", capital="Toronto"))    # nopep8 E501

    data = dict(province='Germany', capital='Berlin')
    print('The capital of {province} is {capital}'.format(**data))

    capital_country = {'US': 'Washington',
                       'Kanada': 'Ottawa',
                       'Deutschland': 'Berlin',
                       'Frankreich': 'Paris',
                       'England': 'London',
                       'Großbritannien': 'London',
                       'Schweiz': 'Bern',
                       'Österreich': 'Wien',
                       'Niederlande': 'Amsterdam'}
    print("\nCountries and their capitals:")
    for c in capital_country:
        format_string = c + ": {" + c + "}"
        print(format_string.format(**capital_country))

    print('\n')
    print('"Training"'.center(20))
    print('"Training"'.center(20, '_'))
    print('"Training"'.ljust(20, '_'))
    print('"Training"'.rjust(20, '_'))

    account_number = "43447879"
    print('Account number:', account_number.zfill(12))


@heading
def myArgsKwargs():

    print('''
Syntax                  Description
--------------------------------------------------------------------------
func(value)             Normal argument: matched by position
func(name=value)        Keyword argument: matched by name
func(*sequence)         Pass all object in sequence as individual positional arguments
func(**dict)            Pass all key/value pairs in dict as individual keyword arguments
def func(name)          Normal argument: matched any passed value by position or name
def func(name=value)    Default argument value, if not passed in the call
def func(*name)         Matches and collects remaining positional arguments in a tuple
def func(**name)        Matches and collects remaining keyword arguments in a dictionary
def func(*args, name)   Arguments that must be passed by keyword only in calls

see: http://www.bogotobogo.com/python/python_functions_def.php
''')

    def fnc(*args, **kwargs):
        print('{} {}'.format(args, kwargs))

    print('\n' * 2)

    print('fnc(*args, **kwargs)')
    print('~' * 20)
    print("{0:37s} {1:>3s}".format('fnc()', ' -> '), end=''), fnc()
    print("{0:37s} {1:>3s}".format('fnc(1, 2, 3)', ' -> '), end=''), fnc(1, 2, 3)
    print("{0:37s} {1:>3s}".format('fnc(1, 2, 3, "flask")', ' -> '), end=''), fnc(1, 2, 3, 'flask')
    print("{0:37s} {1:>3s}".format('fnc(a=1, b=2, c=3)', ' -> '), end=''), fnc(a=1, b=2, c=3)
    print("{0:37s} {1:>3s}".format('fnc(a=1, b=2, c=3, d="ansible")', ' -> '), end=''), fnc(a=1, b=2, c=3, d='ansible')
    print("{0:37s} {1:>3s}".format('fnc(1, 2, 3, a=1, b=2, c=3)', ' -> '), end=''), fnc(1, 2, 3, a=1, b=2, c=3)

    lst = [1, 2, 3]
    tpl = (4, 5, 6)
    dct = {'a': 7, 'b': 8, 'c': 9}
    print("{0:37s} {1:>3s}".format('fnc(*lst, **dct)', ' -> '), end=''), fnc(*lst, **dct)
    print("{0:37s} {1:>3s}".format('fnc(*tpl, **dct)', ' -> '), end=''), fnc(*tpl, **dct)
    print("{0:37s} {1:>3s}".format('fnc(1, 2, *lst)', ' -> '), end=''), fnc(1, 2, *lst)
    print("{0:37s} {1:>3s}".format('fnc(1, 2, *tpl)', ' -> '), end=''), fnc(1, 2, *tpl)
    print("{0:37s} {1:>3s}".format('fnc("jupyter", **dct)', ' -> '), end=''), fnc('jupyter', **dct)
    print("{0:37s} {1:>3s}".format('fnc(arg="django", **dct)', ' -> '), end=''), fnc(arg='django', **dct)
    print("{0:37s} {1:>3s}".format('fnc(1, 2, *tpl, q="bottle", **dct)', ' -> '), end=''), fnc(1, 2, *tpl, q='bottle', **dct)

    print('\n' * 2)

    def fnc2(arg1, arg2, *args, **kwargs):
        print('{} {} {} {}'.format(arg1, arg2, args, kwargs))

    print('fnc2(arg1, arg2, *args, **kwargs)')
    print('~' * 35)
    print("{0:37s} {1:>3s}".format('fnc2()', ' -> '), end=''), print('*** error *** -> cause not positional argument (arg1, arg2) is given')
    print("{0:37s} {1:>3s}".format('fnc2(1, 2)', ' -> '), end=''), fnc2(1, 2)
    print("{0:37s} {1:>3s}".format('fnc2(1, 2, 3, "haystack")', ' -> '), end=''), fnc2(1, 2, 3, 'haystack')
    print("{0:37s} {1:>3s}".format('fnc2(arg1=1, arg2=2, c=3)', ' -> '), end=''), fnc2(arg1=1, arg2=2, c=3)
    print("{0:37s} {1:>3s}".format('fnc2(arg1=1, arg2=2, c=3, d="Spark")', ' -> '), end=''), fnc2(arg1=1, arg2=2, c=3, d='Spark')
    print("{0:37s} {1:>3s}".format('fnc2(1, 2, 3, a=1, b=2)', ' -> '), end=''), fnc2(1, 2, 3, a=1, b=2)
    print("{0:37s} {1:>3s}".format('fnc2(*lst, **dct)', ' -> '), end=''), fnc2(*lst, **dct)
    print("{0:37s} {1:>3s}".format('fnc2(*tpl, **dct)', ' -> '), end=''), fnc2(*tpl, **dct)
    print("{0:37s} {1:>3s}".format('fnc2(1, 2, *tpl)', ' -> '), end=''), fnc2(1, 2, *tpl)
    print("{0:37s} {1:>3s}".format('fnc2(1, *tpl, d="nltk")', ' -> '), end=''), fnc2(1, *tpl, d='nltk')
    print("{0:37s} {1:>3s}".format('fnc2(1, 2, *tpl, d="scikit")', ' -> '), end=''), fnc2(1, 2, *tpl, d='scikit')


if __name__ == '__main__':
    myDict()
    myLogging()
    myEnum()
    myDataTypes()
    myMap()
    myFilter()
    myConst()
    main_timeit.main_timeit()
    myStringFormatting()
    myArgsKwargs()
