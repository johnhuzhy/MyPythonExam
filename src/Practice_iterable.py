# range
# range(start, stop[, step]) -> range object
lst = list(range(0, 100, 3))
print('lst:', lst)

# zip
# zip(iter1 [,iter2 [...]]) --> zip object
a = [1, 3, 5, 7, 9]
b = [27, 26, 25, 24, 23]
c = []
for x, y in zip(a, b):
    c.append(x + y)
print('c:', c)

xdict = {"Nanjing": "025", "Shanghai": "021", "Beijing": "010"}
ydict = dict(zip(xdict.values(), xdict.keys()))
print('ydict=>', ydict.items())

# enumerate
#enumerate(iterable, start=0)
seasons = ['春', '夏', '秋', '冬']
print('season=>', list(enumerate(seasons)))
