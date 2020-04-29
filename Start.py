import decimal
import math

print("Hello World!")

print(id(33))
print(type(3.22222))

print(9.8 * -7.2)
print(2e3)
print(5//2)

a = decimal.Decimal(10.0)
b = decimal.Decimal(3)
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a**b)
# divmod(9/2)

print(math.pi)

print("以下の数字を入力してください：")
x = decimal.Decimal(input('x = '))
y = decimal.Decimal(input('y = '))
print('%d + %d = %d' % (x, y, x+y))
print('%d - %d = %d' % (x, y, x-y))
print('%d * %d = %d' % (x, y, x*y))
print('%d / %d = %d' % (x, y, x/y))
print('%d // %d = %d' % (x, y, x//y))
print('%d %% %d = %d' % (x, y, x%y))
print('%d ** %d = %d' % (x, y, x**y))