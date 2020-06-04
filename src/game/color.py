from enum import Enum, unique
from random import randint


@unique
class Color(Enum):
    """色クラス"""
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def get_random_color():
        """ランダム色を取得"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return(r, g, b)
