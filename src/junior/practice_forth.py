"""
1.正整数を入力して、それが素数かどうかを判別します。
素数は、1とそれ自体でのみ除算できる1より大きい整数を指します。
"""
from math import sqrt
print('*'*33)
num = int(input('正整数を入力してください：'))
if num > 0:
    is_prime = True
    end = int(sqrt(num))
    for i in range(2, end+1):
        if(num % i == 0):
            is_prime = False
            break
    if is_prime:
        print(('{0}は素数です').format(num))
    else:
        print(('{0}は素数ではない').format(num))
else:
    print('正整数ではない')

"""
2.2つの正の整数を入力し、それらの最大公約数と最小公倍数を計算します。
"""
print('*'*33)
print('2つの正の整数を入力してください。')
x = int(input('x = '))
y = int(input('y = '))
if y > x:
    # 通过下面的操作将y的值赋给x, 将x的值赋给y
    (x, y) = (y, x)
for i in range(y, 0, -1):
    if x % i == 0 and y % i == 0:
        print(('{0}と{1}の最大公約数は{2}').format(x, y, i))
        break
# print(('{0}と{1}の最小公倍数は{2}').format(x, y, x * y / i))
for j in range(x, x * y + 1, i):
    if j % x == 0 and j % y == 0:
        print(('{0}と{1}の最小公倍数は{2}').format(x, y, j))
        break
print('*'*33)
