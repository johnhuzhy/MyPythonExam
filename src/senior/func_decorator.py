# Decorator デコレーター
import time


def print_time():
    print(time.time())


def f1():
    print('this is f1!')


# print_time()
# f1()
# ①
def pre_f1(func):
    print_time()
    func()


# ②
def decorator(func):
    def wrapper():
        print_time()
        func()
    return wrapper


# ③
@decorator
def f3():
    print('this is f3!')


# ④
def decoratorx(func):
    def wrapper(*args, **kw):
        print_time()
        func(*args, **kw)
    return wrapper


@decoratorx
def fun1(name):
    print('this is', name)


@decoratorx
def fun2(name1, name2):
    print('this is', name1)
    print('this is', name2)

@decoratorx
def fun3(name1, name2, **kw):
    print('this is', name1)
    print('this is', name2)
    print(kw)


if __name__ == "__main__":
    # # ①
    # pre_f1(f1)
    # # ②
    # f2 = decorator(f1)
    # f2()
    # # ③
    # f3()
    # ④
    fun1('Chromium')
    fun2('Manganum', 'Ferrum')
    fun3('Cobaltum', 'Niccolum', Co=27, Ni=29, ego='latina')
