import timeit
import functools


RANGE_SIZE = 100_000_000
COUNT = 1_000_000
REPEAT = 3
USECS = 1_000_000


def costly_func1():
    m = map(lambda x: x**2, range(RANGE_SIZE))
    return(m)


def costly_func2(lst):
    m = map(lambda x: x**2, lst)
    return(m)


def show_multiple_result(results):
    '''
    result: list of floats
    '''
    global COUNT, REPEAT

    for rslt in results:
        print('{:8.4f} sec/overall {:8.4f} sec/pass {:8.4f} usec/funcCall'.format(rslt, rslt / REPEAT, rslt / REPEAT / COUNT * USECS))


def main_timeit():
    tm = timeit.Timer(costly_func1)
    print('Results for costly_func1:')
    show_multiple_result(tm.repeat(REPEAT, COUNT))

    tm = timeit.Timer(functools.partial(costly_func2, range(RANGE_SIZE)))
    print('\nResults for costly_func2:')
    show_multiple_result(tm.repeat(REPEAT, COUNT))


if __name__ == '__main__':
    main_timeit()
