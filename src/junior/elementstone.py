# coding:utf-8
from random import random
from util import log
"""
Level 1 Elements Stone
"""
l1_value = 0.75  # 0.75 Gold
l1_value_diamond = 8  # 8 Diamond

"""
Level 1 -> Level 3 Elements Stone
"""
l1_to_l3 = 12  # 12 level 1 ES + level1 ES
l1_to_l3_value = 0.39  # 0.39 Gold
l1_to_l3_strength = 10  # 10 Strength

"""
Level 3 -> Level 4 Elements Stone
"""
l3_to_l4 = 16  # 16 level1 ES + level3 ES
l3_to_l4_value = 0.897  # 0.897 Gold
l3_to_l4_strength = 10  # 10 Strength
# Probability of success. If failed, lost all except strength.
l3_to_l4_rate = 0.4878

"""
Level 4 -> Level 6 Elements Stone
"""
l4_to_l6 = 12  # 12 level4 ES + level4 ES
l4_to_l6_value = 19.75  # 0.897 Gold
l4_to_l6_strength = 10  # 10 Strength


def create_l1ES(num=1):
    """Create Level 1 Elements Stone"""
    gold = float(num * l1_value)
    diam = float(num * l1_value_diamond)
    return (gold, diam)


def create_l3ES(num=1):
    """Create Level 3 Elements Stone"""
    gold, diam = create_l1ES(num * (l1_to_l3 + 1))
    gold += float(num * l1_to_l3_value)
    steg = float(num * l1_to_l3_strength)
    return (gold, diam, steg)


def create_l4ES(num=1):
    """Create Level 4 Elements Stone"""
    created = 0
    gold, diam, steg = 0, 0, 0
    while created < num:
        gold_l3, diam_l3, steg_l3 = create_l3ES()
        gold_l1, diam_l1 = create_l1ES(l3_to_l4)
        gold += gold_l3 + gold_l1 + l3_to_l4_value
        diam += diam_l3 + diam_l1
        steg += steg_l3
        success = random()
        if success >= l3_to_l4_rate:
            # Success
            created += 1
            steg += l3_to_l4_strength
        else:
            # Fail
            pass
    return (gold, diam, steg)


def create_l6ES(num=1):
    """Create Level 6 Elements Stone"""
    gold, diam, steg = create_l4ES(num * (l4_to_l6 + 1))
    gold += num * l4_to_l6_value
    steg += num * l4_to_l6_strength
    return (gold, diam, steg)


"""
level6 ES ~~ 750 Gold
1 Diamond = 0.75 Gold
1 Strength = 1 Gold
"""
l6ES_worth = 750
if __name__ == "__main__":
    l6_num = 10
    # 低次石を使えて生成する
    gold, diam, steg = create_l6ES(l6_num)
    complicated = gold + diam * 0.75 + steg
    # 直接に黄金を使える
    gold_cost = l6ES_worth * l6_num
    if complicated > gold_cost:
        print('直接に黄金を使えれば、効果は高い')
    else:
        print('低次石を使えて生成すれば、効果は高い')
