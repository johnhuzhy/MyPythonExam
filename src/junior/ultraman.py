# coding=utf-8
from abc import ABCMeta, abstractmethod
from random import randint, randrange
"""
ウルトラマンとモンスター
"""


class Fighter():
    """ ファイター """
    # __slots__制限
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        """
        初期化メソッド
        :param name: 名前
        :param hp: ヒットポイント
        """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """
        攻撃する
        :param other: 攻撃されたもの
        """
        pass


class Ultraman(Fighter):
    """ ウルトラマン """
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(20, 25)

    def huge_attack(self, other):
        """
        究極必杀技(打掉对方至少50点或四分之三的血)
        :param other: 被攻击的对象
        :return: 使用成功返回True否则返回False
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        """
        魔法攻击
        :param others: 被攻击的群体
        :return: 使用魔法成功返回True否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        """恢複魔法值"""
        incr_mp = randint(3, 10)
        self._mp += incr_mp
        return incr_mp

    def __str__(self):
        return f'~~~{self._name}奥特曼~~~\n  生命值: {self._hp}\n  魔法值: {self._mp}'


class Monster(Fighter):
    """モンスター"""
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return f'~~~{self._name}小怪兽~~~\n  生命值: {self._hp}\n'


def is_any_alive(monsters):
    """判断有没有小怪兽是活着的"""
    for temp in monsters:
        if temp.alive:
            return True
    else:
        return False


def select_one_alive(monsters):
    """选中一只活着的小怪兽"""
    mon_lens = len(monsters)
    while True:
        index = randrange(mon_lens)
        temp = monsters[index]
        if temp.alive:
            return temp


def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


if __name__ == "__main__":
    u = Ultraman('Huzhy', 500, 100)
    m1 = Monster('狄仁杰', 250)
    m2 = Monster('白元芳', 300)
    m3 = Monster('王大锤', 250)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('#'*15, f"第{fight_round:02}回合", '#'*15)
        m = select_one_alive(ms)
        skill = randint(1, 10)
        if skill <= 6:  # 60%的概率使用普通攻击
            print(f'{u.name}使用普通攻击打了{m.name}.')
            u.attack(m)
            print(f'{u.name}的魔法值回復了{u.resume()}点.')
        elif skill <= 9:  # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
            if u.magic_attack(ms):
                print(f'{u.name}使用了魔法攻击.')
            else:
                print(f'{u.name}使用魔法失败.')
        else:  # 10%的概率使用究極必杀技(如果魔法值不足则使用普通攻击)
            if u.huge_attack(m):
                print(f'{u.name}使用究極必杀技虐了{m.name}.')
            else:
                print(f'{u.name}使用普通攻击打了{m.name}.')
                print(f'{u.name}的魔法值回復了{u.resume()}点.')
        if m.alive:  # 如果选中的小怪兽没有死就回击奥特曼
            print(f'{m.name}回击了{u.name}.')
            m.attack(u)
        display_info(u, ms)  # 每个回合结束后显示奥特曼和小怪兽的信息
        fight_round += 1
    print("="*15, "战斗结束!", "="*15)
    if u.alive:
        print(f'{u.name}奥特曼勝利!')
    else:
        print('小怪兽勝利!')
