from operator import add, mul, sub, truediv
import time


def memoize(func):
    cache = {}

    def memoized(*args):
        if args not in cache: cache[args] = func(*args)
        return cache[args]
    return memoized


def recur_pow(num1, num2, res=1):
    oper, oper2 = (sub, mul) if num2 > 0 else (add, truediv)
    return (recur_pow(num1, oper(num2, 1), oper2(res, num1)) 
            if abs(num2) > 0 else res)


@memoize
def fib(n):
    return fib(n - 1) + fib(n - 2) if n > 1 else n
