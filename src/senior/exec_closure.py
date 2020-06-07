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

a = 2
fn = curve_pre()
# タイプ
print(type(fn))
print(fn(7))
# 環境変数
print(fn.__closure__)
print(fn.__closure__[0].cell_contents)
print('#'*33)

def f1():
    a = 12
    def f2():
        a = 13
        print(a)
    print(a)
    f2()
    print(a)

f1()
