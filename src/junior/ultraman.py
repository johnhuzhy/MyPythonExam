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

    def attack(self, other):
        """
        攻撃する
        """
        fb = randint(1, 10)
        if fb >= 8:
            self.fatal_blow(other)
        else:
            self.normal_attack(other)

    @abstractmethod
    def fatal_blow(self, other):
        """
        致命的な打撃
        :param other: 攻撃されたもの
        """
        pass

    @abstractmethod
    def normal_attack(self, other):
        """
        一般的な攻撃
        :param other: 攻撃されたもの
        """
        pass


class Ultraman(Fighter):
    """ ウルトラマン """
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def normal_attack(self, other):
        other.hp -= randint(20, 25)

    def fatal_blow(self, other):
        injury = randint(40, 60)
        other.hp -= injury
        print(f'◆◆◆ {self._name}奥特曼は致命的な打撃を与える({injury}) ◆◆◆')

    def huge_attack(self, other):
        """
        究極必殺技(打掉对方至少50点或四分之三的血)
        :param other: 被攻撃的对象
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
        魔法攻撃
        :param others: 被攻撃的群体
        :return: 使用魔法成功返回True否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(15, 30)
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

    def normal_attack(self, other):
        other.hp -= randint(10, 20)

    def fatal_blow(self, other):
        if int(self._hp * 0.1) > 5:
            blood = randint(5, int(self._hp * 0.1))
            injury = randint(10, 20) + int(blood * 1.8)
            self._hp -= blood
            other.hp -= injury
            print(f'◇◇◇　{self._name}小怪獸は血撃を与える({blood}↢↣{injury})　◇◇◇')
        else:
            self.normal_attack(other)

    def __str__(self):
        if self.alive:
            return f'~~~{self._name}小怪獸~~~\n  生命值: {self._hp}\n'
        else:
            return f'~~~{self._name}は殺された~~~\n'


def is_any_alive(monsters):
    """判断有没有小怪獸是活着的"""
    for temp in monsters:
        if temp.alive:
            return True
    else:
        return False


def select_one_alive(monsters):
    """選擇一只活着的小怪獸"""
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
    u = Ultraman('Huzhy', 800, 100)
    m1 = Monster('牛魔王', 250)
    m2 = Monster('白骨精', 200)
    m3 = Monster('犀牛精', 350)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('#'*15, f"第{fight_round:02}回合", '#'*15)
        m = select_one_alive(ms)
        skill = randint(1, 10)
        if skill <= 6:  # 60%的概率使用普通攻撃
            print(f'{u.name}使用普通攻撃打了{m.name}.')
            u.attack(m)
            print(f'{u.name}的魔法值回復了{u.resume()}点.')
        elif skill <= 9:  # 30%的概率使用魔法攻撃(可能因魔法值不足而失败)
            if u.magic_attack(ms):
                print(f'{u.name}使用了魔法攻撃.')
            else:
                print(f'{u.name}使用魔法失败.')
                print(f'{u.name}使用普通攻撃打了{m.name}.')
                u.attack(m)
        else:  # 10%的概率使用究極必殺技(如果魔法值不足则使用普通攻撃)
            if u.huge_attack(m):
                print(f'{u.name}使用§究極必殺技§虐了{m.name}.')
            else:
                print(f'{u.name}使用普通攻撃打了{m.name}.')
                print(f'{u.name}的魔法值回復了{u.resume()}点.')
        if is_any_alive(ms):  # 如果小怪獸没有死就回击奥特曼
            for mst in ms:
                if mst.alive:
                    print(f'{mst.name}回击了{u.name}.')
                    mst.attack(u)
        display_info(u, ms)  # 每个回合结束后显示奥特曼和小怪獸的信息
        fight_round += 1
    print("="*15, "战斗结束!", "="*15)
    if u.alive:
        print(f'{u.name}奥特曼勝利!')
    else:
        print('小怪獸勝利!')
