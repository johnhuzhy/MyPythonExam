def r_return(n):
    print("You taked me.")
    while n > 0:
        print("before return")
        return n
        n -= 1
        print("after return")

def y_yield(n):
    print("You taked me.")
    while n > 0:
        print("before return")
        yield n
        n -= 1
        print("after return")

def fib(max):
    """
    fibnaticc
    """
    n, a, b = 0,0,1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1

if __name__ == "__main__":
    rr = r_return(3)
    print(rr)
    yy = y_yield(3)
    yy.__next__()
    # print(yy)
    yy.__next__()
    # print(yy)
    # yy.__next__()
    # print(yy)
    f = fib(13)
    for i in f:
        print(i,end=',')
