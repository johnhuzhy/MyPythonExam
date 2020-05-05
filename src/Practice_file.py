# coding:utf-8
import fileinput
f = open('./prop/505.txt', "a+")
for line in f:
    print(line, end='')
f.write("\nLife is short, you nedd python.")
f.close()

print('#'*33)
# with
with open("./prop/505.txt")as fp:
    print(fp.read())

print('#'*33)
# fileinput
for line in fileinput.input('./prop/505.txt'):
    print(line, end='')

print('#'*33)
#readline seek
f = open('./prop/505.txt')
print(f.readline())
print(f.readline())
f.seek(0)
print(f.readline())