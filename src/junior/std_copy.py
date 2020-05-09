import copy
# copy.__all__
# ['Error', 'copy', 'deepcopy']


class TestCopy:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


if __name__ == "__main__":
    foo = TestCopy(7)

    a = ["foo", foo]
    b = a[:]
    c = list(a)
    d = copy.copy(a)
    e = copy.deepcopy(a)

    a.append("shan")
    foo.value = 17

    print(f"orginal:{a}")
    print(f"silce:{b}")
    print(f"list:{c}")
    print(f"copy:{d}")
    print(f"deepcopy:{e}")
