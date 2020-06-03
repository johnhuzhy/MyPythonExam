# coding=utf-8
import random


class Person():
    """
    A sample of class
    """

    def __init__(self, name):
        self.name = name
        # print(self)
        # print(type(self))

    def get_name(self, age):
        # return self.name
        if self.select(age):
            return self.name
        else:
            return "the name is secret"

    @staticmethod
    def select(n):
        a = random.randint(1, 100)
        return a - n > 0

    def breast(self, num):
        self.breast = num

    def color(self, color):
        print(f"{self.name}\'s hair is {color}")

    def how(self):
        print(f"{self.name} breast is {self.breast}")


if __name__ == "__main__":
    girl = Person("Shanshan")
    # print(girl)
    # print(type(girl))
    # print(girl.name)
    girl.breast(90)
    girl.color("black")
    girl.how()

    f = Person("Stella")
    name = f.get_name(27)
    print("name:", name)
