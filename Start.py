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
# print('%d + %d = %d' % (x, y, x+y))
print(('{0} + {1} = {2}').format(x, y, x+y))
# print('%d - %d = %d' % (x, y, x-y))
print(('{0} - {1} = {2}').format(x, y, x-y))
print(('{0} * {1} = {2}').format(x, y, x*y))
print(('{0} / {1} = {2}').format(x, y, x/y))
print(('{0} // {1} = {2}').format(x, y, x//y))
print(('{0} % {1} = {2}').format(x, y, x % y))
print(('{0} ** {1} = {2}').format(x, y, x**y))

alst = [1,2,3,4,5,6,7]
print(alst[::-1])
print(alst)
#append<->extend
alst.append(["john","github"])
print(alst)

blst = [1,2,3,4,5,6,7]
blst.extend(["john","github"])
print(blst)

#str
#'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 
#'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 
#'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 
# 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'

line = "Hello. I am John. Welcome you." 
lst = line.split()
print(lst[:])
"$".join(lst)
print(lst[:])