from enum import Enum, IntEnum, unique


class VIP(Enum):
    """列挙型：VIPのタイプである"""
    # key 重複出来ない
    YELLOW = '1'
    RED = '2'
    BLACK = '3'
    GREEN = '4'
    GREEN_ALIAS = '4'


@unique
class QQVIP(IntEnum):
    """数値列挙型"""
    # バリュー Int & 重複出来ない
    YELLOW = 1
    RED = 2
    BLACK = 3
    GREEN = '4'


def fun1_2():
    """出力、列挙型の特徴"""
    print(type(VIP.YELLOW), ":", VIP.YELLOW)
    # Cannot reassign members.
    # VIP.RED = '8'


def fun3():
    """キー、名前、バリュー"""
    print(type(VIP.YELLOW.name), ":", VIP.YELLOW.name)
    print(f"{VIP['RED']} = {VIP.RED.value}")
    print(f"{VIP.BLACK.name} = {VIP.BLACK.value}")
    print('~'*33)
    for v in VIP:
        print(f"{v} : {v.name} = {v.value}")


def fun4():
    """等しい、比較"""
    r1 = VIP.BLACK == VIP.BLACK
    print(r1)
    r2 = VIP.BLACK is VIP.BLACK
    print(r2)


def fun5():
    """重複なラベル"""
    for v in VIP.__members__.items():
        print(v)
    for v in VIP.__members__:
        print(v)


def fun6():
    """Value ⇒ Key"""
    r = '2'
    print(VIP(r))


def fun7():
    """数値列挙型"""
    print(QQVIP.RED)
    print(type(QQVIP.GREEN.value), ":", QQVIP.GREEN.value)


if __name__ == "__main__":
    fun1_2()
    fun3()
    fun4()
    fun5()
    fun6()
    fun7()
