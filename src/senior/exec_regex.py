# coding=utf-8
# 正規表現
# 正規表現の中心は「規則」である
import re

str_all = 'C5C++2Java4Python8C# 5Java&Script3_Ruby\nPHP'
str_set = r'abc,acc,ahc,aec,afc,adc'
str_all2 = 'pytho0python1pythonn2pythonx3'
str_qq = '1234567890ec123456789py1234jp234567'


def fun_c1():
    """
    検索 String 普通字符
    """
    str_py = 'Python'
    # print(str_all.index(str_py) > -1)
    print(str_py in str_all)
    print(re.findall(str_py, str_all))
    if len(re.findall(str_py, str_all)) > 0:
        print(str_py, 'はある')


def fun_c2():
    """
    検索 数値 非数値
    """
    str_num = '\d'  # 数値
    print(re.findall(str_num, str_all))
    str_alf = '\D'  # 非数値
    print(re.findall(str_alf, str_all))


def fun_c3():
    """
    検索 元字符
    """
    str_c1 = 'a[c|f]c'
    print(re.findall(str_c1, str_set))
    str_c2 = 'a[c-f]c'
    print(re.findall(str_c2, str_set))


def fun_c4():
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


def fun_c567():
    """
    数量詞
    """
    str_su = '[A-Za-z]{3,6}'  # 贪婪
    print(re.findall(str_su, str_all))
    str_sr = '[A-Za-z]{3,6}?'  # 非贪婪
    print(re.findall(str_sr, str_all))
    str_s0 = 'python*'  # *:[0→∞]
    print(re.findall(str_s0, str_all2))
    str_s1 = 'python+'  # +:[1→∞]
    print(re.findall(str_s1, str_all2))
    str_s2 = 'python?'  # ?:[0,1]
    print(re.findall(str_s2, str_all2))


def fun_c8():
    """
    辺界匹配
    """
    str_n1 = '^\d{5,9}$'  # 5~9桁数字
    str_nt = '570608097'
    str_ne = '10001'
    print(re.findall(str_n1, str_nt))
    print(re.findall(str_n1, str_ne))
    nl = re.findall('[0-9]+', str_qq)
    for str in nl:
        print(re.findall(str_n1, str))


def fun_c9():
    """
    組検索
    """
    str_jf = 'pythonpythonpythonpythonpython'
    str_pt = '(python){2}'
    print(re.findall(str_pt, str_jf))


def fun_c10():
    """
    検索模式
    """
    language = 'basic\nc#javarubypython'
    str_pt = '.{1}C#'
    print(re.findall(str_pt, language, re.I))  # 忽略大小写
    print(re.findall(str_pt, language, re.I | re.S))  # .可以匹配\n


def convert11(value):
    """
    サンプル置換えファクション
    """
    print(value)
    matched = value.group()
    return '!!' + matched + '!!'


def convert12(value):
    """
    数字置換えファクション
    """
    matched = value.group()
    if int(matched) >= 6:
        return '9'
    else:
        return '0'


def fun_f11():
    """
    re.sub置換え
    """
    rl = re.sub('C#', convert11, str_all)
    print(rl)
    r2 = re.sub('python', 'javascript', str_all2, 2)
    print(r2)
    f12 = re.sub('\d', convert12, str_qq)
    print(f12)


def fun_f13():
    """
    re.match re.search
    """
    r1 = re.match('\d', str_all)
    print(r1)
    r2 = re.search('\d', str_all)
    print(r2.group())
    r3 = re.match('\d', str_qq)
    print(r3.span())


def fun_f14():
    """
    search group分組
    """
    str_f14 = "Life is short, I use python, I love python"
    r = re.search('Life(.*)python(.*)python', str_f14)
    print(r.group(0))
    print(r.group(1))
    print(r.group(2))
    print(r.groups())
    rf = re.findall('Life(.*)python', str_f14)
    print(rf)


if __name__ == "__main__":
    fun_c1()
    fun_c2()
    fun_c3()
    fun_c4()
    fun_c567()
    fun_c8()
    fun_c9()
    fun_c10()
    fun_f11()
    fun_f13()
    fun_f14()
