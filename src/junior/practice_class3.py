# coding=utf-8
class Rectangle:
    """
    the wiedth and length of Rectangle
    """

    def __init__(self):
        self.width = 0
        self.length = 0

    def __setattr__(self, name, value):
        if name == "size":
            self.width, self.length = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if name == "size":
            return self.width, self.length
        else:
            raise AttributeError

    # def setSize(self, size):
    #     self.width, self.length = size

    # def getSize(self):
    #     return self.width, self.length


if __name__ == "__main__":
    r = Rectangle()
    r.width = 3
    r.length = 4
    print(r.size)
    r.size = (30, 40)
    print(r.width)
    print(r.length)
