# coding=utf-8
import math


class Point:
    """
    平面上のポイントを記述するクラスを定義し、
    ポイントを移動して別のポイントまでの距離を計算するメソッドを提供する
    """

    def __init__(self, x=0, y=0):
        """
        ポイント初期化
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """
        指定された場所に移動する
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """
        指定された増分を移動する
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """
        別のポイントからの距離を計算する
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

    def __str__(self):
        return f"({self.x}, {self.y})"


if __name__ == "__main__":
    p1 = Point(2, 3)
    print("p1->",p1)
    p2 = Point()
    print("p2->",p2)
    p2.move_by(-1,5)
    print("p2->",p2)
    print(p1.distance_to(p2))
