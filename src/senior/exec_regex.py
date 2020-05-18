# coding=utf-8
# 正規表現
# 正規表現の中心は「規則」である
import re

str_all = 'C5C++2Java4Python8C# 5Java&Script3_Ruby\nPHP'
str_set = r'abc,acc,ahc,aec,afc,adc'

if __name__ == "__main__":
    """
    検索 String 普通字符
    """
    str_py = 'Python'
    # print(str_all.index(str_py) > -1)
    print(str_py in str_all)
    print(re.findall(str_py, str_all))
    if len(re.findall(str_py, str_all)) > 0:
        print(str_py, 'はある')

    """
    検索 数値 非数値
    """
    str_num = '\d'  # 数値
    print(re.findall(str_num, str_all))
    str_alf = '\D'  # 非数値
    print(re.findall(str_alf, str_all))

    """
    検索 元字符
    """
    str_c1 = 'a[c|f]c'
    print(re.findall(str_c1, str_set))
    str_c2 = 'a[c-f]c'
    print(re.findall(str_c2, str_set))

    """
    検索 概括字符集
    """
    str_d = '[0-9]'  # 数値
    print(re.findall(str_d, str_all))
    str_D = '[^0-9]'  # 非数値
    print(re.findall(str_D, str_all))
    str_w = '\w'  # 字符
    print(re.findall(str_w, str_all))
    str_w1 = '[A-Za-z0-9_]'  # 字符
    print(re.findall(str_w1, str_all))
    str_W = '\W'  # 非字符
    print(re.findall(str_W, str_all))
    str_W2 = '[^A-Za-z0-9_]'  # 非字符
    print(re.findall(str_W2, str_all))
    str_s = '\s'  # 空白字符
    print(re.findall(str_s, str_all))
    str_S = '\S'  # 非空白字符
    print(re.findall(str_S, str_all))






