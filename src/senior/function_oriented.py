from functools import reduce
# 関数指向プログラミング
a = 1
b = 2

lx = [x**2 for x in range(13)]
ly = [y for y in range(20, 33)]
lz = [str(x) for x in lx]

if __name__ == "__main__":
    # Trinocular expression 三眼式
    rl = a if a > b else b
    print(rl)

    # map
    lr = map(lambda x, y: x if x > y else y, lx, ly)
    print(list(lr))

    # reduce
    ls = reduce(lambda x, y: x + y, lx)
    print(ls)
    it = 0
    for x in lx:
        it += x
    print(it)
    # reduce
    lu = reduce(lambda x, y: x + y, lz, 'init')
    print(lu)

    # filter
    la = filter(lambda x : x > 99, lx)
    print(list(la))

    
