"""
指定した長さの検証コードを生成する関数を設計します。検証コードは、大文字と小文字および数字で構成されます。
"""
import random


def generate_code(length=6):
    """
    指定した長さの検証コードを生成する。
    """
    all_str = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    code = ''
    for i in range(length):
        index = random.randint(0, len(all_str)-1)
        code += all_str[index]
    return code


"""
パスカルの三角形(杨辉三角形)
"""


def pascal_triangle(num=6):
    """
    パスカルの三角形（Pascal's triangle）は、二項展開における係数を三角形状に並べたものである
    """
    triagle = [[]] * num
    for row in range(num):
        triagle[row] = [None] * (row+1)
        print(' '*(len(str(num**2))-1)*(num - row), end='')
        for col in range(row+1):
            if col == 0 or col == row:
                triagle[row][col] = 1
            else:
                triagle[row][col] = triagle[row-1][col-1] + triagle[row-1][col]
            print(str(triagle[row][col]).center(len(str(num**2)), ' '), end=' ')
        print()


if __name__ == "__main__":
    print("検証コード⇒", generate_code(8))
    pascal_triangle(13)
