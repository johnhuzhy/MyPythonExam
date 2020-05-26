# coding=utf-8
def times(x, y=2):
    print(("x = {}").format(x))
    print(("y = {}").format(y))
    return x * y


z = times('shan', 3)
print("z = ", z)


def fibonacci(n):
    """
    これはフィボナッチ数列です
    """
    lst = [0, 1]
    for i in range(n-2):
        lst.append(lst[-2]+lst[-1])
    return lst


fl = fibonacci(10)
print(fl)

m = {0: 0, 1: 1}


def fib(n):
    if not n in m:
        m[n] = fib(n-1)+fib(n-2)
    return m[n]


fm = fib(10)
print(fm)


def naming():
    '''global name'''
    global c
    c = '33'


naming()
print(c)
