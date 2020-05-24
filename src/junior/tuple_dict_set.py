from math import pi
# list
#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
hlst= ['2', 'x', 'github.co.jp']
hlst.sort()
print('hlst.sort()=>', hlst)
print('hlst[:-1]:', hlst[:-1])
ilst=['java','ruby','c++']
hlst=hlst + ilst * 3
hlst.reverse()
print('hlst.reverse()=>:',hlst)
print('hlst.index(\'x\'):', hlst.index('x'))
hlst.append(ilst)
print('hlst.append(ilst):', hlst)
hlst.extend(ilst)
print('hlst.extend(ilst):', hlst)
print('hlst.count(\'ruby\'):', hlst.count('ruby'))
hlst.insert(3, 'Hurry')
print('len(hlst):',len(hlst))
print('hlst.remove(\'c++\'):',hlst.remove('c++'))
print('hlst.pop():',hlst.pop())

print('#'*33)
# tuple
#'count', 'index'
t = (1,'23',[123,'abc'],('python','learn'))
print('t[1:]=',t[1:])
print('t.count(\'23\')=', t.count('23'))
print('t.index([123,\'abc\'])=', t.index([123,'abc']))

print('#'*33)
# dict
#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
xdict = {'name': 'hu', 'age': '33', 'sex': 'male'}
ydict = dict(name='stella', age=26, phone='123456', sex='female')
print(xdict)
print('xdict[\'name\']:', xdict['name'])
print('len(xdict):', len(xdict))
print('xdict[\'age\']:', xdict.get('age'))
print('ydict.pop(\'age\'):', ydict.pop('age'))
print('ydict.popitem:', ydict.popitem())
xdict.update(ydict)
print('xdict.update(ydict)=>', xdict.items())
print('xydict:', ydict.values())

print('#'*33)
# set
#'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint',
#'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'
aset = set(['q', 'i', 's', 'r', 'w'])
bset = set(['a', 'q', 'i', 'h', 'u'])
print("aset == bset :", aset == bset)
cset = set(['a', 'h'])
print("cset.issubset(bset):", cset.issubset(bset))
print("aset.issuperset(cset):", aset.issuperset(cset))
print("aset.union(bset):", aset.union(bset))
print("aset.intersection(bset):", aset.intersection(bset))
print("aset.difference(bset):", aset.difference(bset))

print('#'*33)
# リスト内包
squares1 = list(map(lambda x: x**2, range(10)))
print(squares1)
squares2 = [x**2 for x in range(10)]
print(squares2)
combs1 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combs1)
combs2 = [(x, x**2, x**3) for x in range(9)]
print(combs2)
px = [str(round(pi, i)) for i in range(1, 9)]
print(px)
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
matrix1 = [[row[i] for row in matrix] for i in range(4)]
print(matrix1)
matrix2 = list(zip(*matrix))
print(matrix2)
