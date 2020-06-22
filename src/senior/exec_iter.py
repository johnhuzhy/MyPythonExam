class BookCollection():
    """イテレータ"""
    def __init__(self):
        self.data=['《源氏物語》','《春秋》','《大学》']
        self.cur= 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur >= len(self.data):
            raise StopIteration()
        r = self.data[self.cur]
        self.cur += 1
        return r 

def gen(max):
    """生成器"""
    n = 0
    while n < max:
        n += 1
        yield n

if __name__ == "__main__":
    books = BookCollection()
    # print(next(books))
    for book in books:
        print(book)
    # for book in books:
    #     print(book)

    g = gen(1000)
    # print(next(g))
    # print(next(g))
    for i in g:
        print(i)
    
    # Generator Object
    n = (i for i in range(1000))
    print(n)