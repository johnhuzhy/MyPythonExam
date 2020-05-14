# encoding=UTF-8
import calendar
import time
import datetime
import locale

# calendar
cal = calendar.month(2020, 5)
print(cal)
# isleap
print("閏年判断(2100)⇒", calendar.isleap(2100))
print("閏年判断(2020)⇒", calendar.isleap(2020))
# weekday
print("weekday:", calendar.weekday(2020, 5, 14))

print('-'*33)
# time
# localtime
lt = time.localtime()
print("localtime⇒", time.localtime())
print(f"{lt[0]}年{lt[1]}月{lt[2]}日:{lt[3]}時{lt[4]}分{lt[5]}秒 ⇒ 今週{lt[6]}日目 ⇒ 今年{lt[7]}日目")
# asctime
print("asctime:", time.asctime())
# strftime
print("年月日⇒", time.strftime('%Y/%m/%d || %B,%d,%y || %x'))
print("時分秒⇒", time.strftime('%H:%M:%S || %p%I:%M:%S || %X'))

print('-'*33)
# datetime
today = datetime.date.today()
print("today:", today)
print("ctime:", today.ctime())
print("weekday:", today.weekday())
# ordinal
to = today.toordinal()
print("ordinal:", datetime.date.fromordinal(to))
# time
tm = datetime.time(2, 3, 4)
print("time:", tm)
# now
now = datetime.datetime.now()
print("now:", now)
# timedelta
h5 = now + datetime.timedelta(hours=5)
print("h5:", h5)
w2 = now + datetime.timedelta(weeks=2)
print("w2:", w2)

print('-'*33)
# weekday
print(now.strftime('%A, %a, %B, %b'))
# 曜日を日本語にする方法
week_name_list='月火水木金土日'
print("日本語曜日:",week_name_list[int(today.weekday())])

locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
print(locale.getlocale(locale.LC_TIME))
print(now.strftime('%A, %a, %B, %b'))

locale.setlocale(locale.LC_TIME, 'ja_JP.UTF8')
print(locale.getlocale(locale.LC_TIME))
print(now.strftime('%A, %a, %B, %b'))
