def fun_8_4():
    a, b, c = 1, 3, 5
    d = 5, 6, 7
    a, b, c = d
    print((a, b, c))


def key_para(x, y, z=0, w=1):
    return z + (x**y)//w


def fun_8_56():
    a = key_para(y=2, x=6)
    print(a)
    b = key_para(4, 3, w=2)
    print(b)
    c = key_para(6, 2, w=3, z=2)
    print(c)


if __name__ == "__main__":
    fun_8_4()
    fun_8_56()
