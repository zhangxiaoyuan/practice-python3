#/usr/bin/env python3.6
# -*- coding:utf-8 -*-

__author__ = 'Jagger'

'''
题目：输入某年某月某日，判断这一天是这一年的第几天？ 
1.程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊 
      情况，闰年且输入月份大于3时需考虑多加一天。 
'''

def func():
	days = (0,31,59,90,120,151,181,212,243,273,304,334)
	
	year = int(input('please input year\n'))
	month = int(input('please input month\n'))
	day = int(input('please input day\n'))
	
	if (month <= 12) and (month >= 1) and (day <= 31) and (day >=1):
		sum_days = days[month - 1]
	else:
		print('input data error')
		return 

	sum_days += day

	leap = False
	if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
		leap = True

	if (leap) and (month > 2):
		sum_days += 1

	print('today is %s days' % sum_days)


func()
	

