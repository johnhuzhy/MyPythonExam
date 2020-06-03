# coding=utf-8
class Foo:
    lang = "Java"

    def __init__(self):
        self.lang = "python"

    @classmethod
    def get_class_attr(cls):
        return cls.lang


if __name__ == "__main__":
    print("Foo.lang:", Foo.lang)
    r = Foo.get_class_attr()
    print("get class attribute:", r)
    f = Foo()
    print("Instance attribute:", f.lang)
    print("Instance get class attribute:", f.get_class_attr())


class Person:
    def __init__(self, name):
        self.name = name

    def height(self, m):
        h = dict((["height", m],))
        return h

    def breast(self, n):
        b = dict((["breast", n],))
        return b


class Girl(Person):
    def get_name(self):
        return self.name


if __name__ == "__main__":
    shan = Girl("shanshan")
    print(shan.get_name())
    print(shan.height(160))
    print(shan.breast(90))

    # def f(x, y): return x+y
    f = lambda x,y : x+y
    print(f(2, 3))
    print(f("hu", "sun"))
    print(f(["c++", "java"], ["delphi", "basic"]))
