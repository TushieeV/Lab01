'''
task = produce list of fibonacci numbers of length n

DIFFICULTY = EASY
TOPICS = lists, variables, loops

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
'''

import math

def produceFibsList(n):
    '''
    >>> produceFibsList(0)
    []
    >>> produceFibsList(1)
    [1]
    >>> produceFibsList(2)
    [1, 1]
    >>> produceFibsList(3)
    [1, 1, 2]
    >>> produceFibsList(5)
    [1, 1, 2, 3, 5]
    '''
    # TODO = fill in the code here, and return the correct result using the return keyword
    listFibs = []

    for i in range(1, n + 1):
        listFibs.append(int(nthFib(i)))

    return listFibs
    pass

def nthFib(n):
    num1 = ((1 + math.sqrt(5)) / 2) ** n
    num2 = ((1 - math.sqrt(5)) / 2) ** n
    num3 = num1 - num2
    fib = num3 / math.sqrt(5)
    return fib

if __name__ == '__main__':
    import doctest
    doctest.testmod()
