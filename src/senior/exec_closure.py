def curve_pre():
    """クロージャー(英語: closure)"""
    # 引数以外の変数を実行時の環境ではなく、自身が定義された環境（静的スコープ）において解決すること
    # 関数ではなくとも、環境に紐付けられたデータ構造のことをクロージャと呼ぶ場合もある。
    a, b, c = 1, 2, 3

    def curve(x):
        print('this is a function!')
        y = a*x*x + b*x + c
        return y
    return curve


def f1():
    a = 12

    def f2():
        a = 13
        print(a)
    print(a)
    f2()
    print(a)


def clsr_trvl(total=0):
    def trvl_go(add):
        nonlocal total
        new_total = total + add
        total = new_total
        return new_total
    return trvl_go


def not_clsr_trvl(x):
    global tol
    new_tol = tol + x
    tol = new_tol
    return new_tol


if __name__ == "__main__":
    a = 2
    fn = curve_pre()
    # タイプ
    print(type(fn))
    print(fn(7))
    # 環境変数
    print(fn.__closure__)
    print(fn.__closure__[0].cell_contents)
    print('#'*33)

    f1()
    print('#'*33)

    tol = 0
    ft = clsr_trvl()
    for idx in range(3):
        a = int(input('ADD='))
        print(not_clsr_trvl(a), "&& tol=", tol)
        print(ft(a), "&& 環境変数=", ft.__closure__[0].cell_contents)
