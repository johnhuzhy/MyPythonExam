"""
１．華氏を摂氏に変換
$C=(F - 32) \div 1.8$
"""
print('華氏を入力してください：')
fa = float(input('fa = '))
ce = (fa - 32) / 1.8
print(('華氏{0:.2f}=摂氏{1:2.2f}').format(fa, ce))

"""
２．年を入力して、閏年かどうかを判断する
"""
print('年を入力してください：')
year = int(input('year = '))
flag = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(('{0}年は閏年か：{1}').format(year, flag))