import os
import shutil
import glob
import sys
import random
import statistics
import doctest


def for_os():
    """lib:os"""
    # getcwd
    print(os.getcwd())
    # chdir
    os.chdir(os.getcwd())
    # system
    # os.system('cls')


def for_shutil():
    """lib:shutil"""
    # copyfile
    shutil.copyfile('./log/2020-05-28.log', './log/2020-05-31.log')
    # move
    shutil.move('./log/2020-05-31.log', './prop/')


def for_glob():
    """lib:glob"""
    # golb
    v = glob.glob('./src/junior/*.py')
    print(type(v), "⇒", v)


def for_random():
    """lib:random"""
    # sample 重複なし
    print(random.sample(range(200), 10))
    # ランダムな少数
    print(random.random())
    # range(33)からランダムに選んだ整数
    print(random.randrange(33))


def for_statistics():
    """lib:statistics"""
    data = [random.random() for x in range(10)]
    # 平均
    print("平均:", statistics.mean(data))
    # 中央値
    print("中央値:", statistics.median(data))
    # 分散
    print("分散:", statistics.variance(data))


if __name__ == "__main__":
    for_os()
    for_shutil()
    for_glob()
    print(sys.argv)
    for i in range(10):
        for_random()
    for_statistics()
    doctest.testmod()
