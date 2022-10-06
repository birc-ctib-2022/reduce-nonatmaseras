"""Reduce and accumulate module"""

from typing import TypeVar, Callable
A = TypeVar('A')
B = TypeVar('B')

def reduce(f: Callable[[A], B], x: list[A]) -> B:
    """
    Reduce f over list x.x

    >>> reduce(lambda x,y: x+y, [1, 2, 3])
    6
    """
    assert len(x) >= 2
    #initialize with the first element
    value = x[0]
    #skip first position
    for i in (1,len(x)-1):
        #accumulate result
        value = f(value, x[i])
    return value
    


def accumulate(f: Callable[[A], A], x: list[A]) -> list[A]:
    """
    Accumulate f over list x.x

    >>> accumulate(lambda x,y: x+y, [1, 2, 3])
    [1, 3, 6]
    """
    assert len(x) >= 2
    values = [0]*len(x)
    #skip first position
    values[0] = x[0]
    for i in range(1,len(x)):
        #accumulate result
        values[i] = f(values[i-1], x[i])
        
    return values


