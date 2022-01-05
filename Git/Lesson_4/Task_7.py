from functools import reduce
from itertools import count
from math import factorial

def factor(n):
    for i in count(1):
        if i <= n:
            result = factorial(i)
            yield result
        else:
            break

for el in factor(10):
    print(el)

def factor(n):
    for i in count(1):
        if i <= n:
            result = reduce(lambda x, y: x*y, range(1, i+1))
            yield result
        else:
            break

for el in factor(10):
    print(el)

def factor(n):
    result = 1
    for i in count(1):
        if i <= n:
            result *= i
            yield result
        else:
            break

for el in factor(10):
    print(el)
