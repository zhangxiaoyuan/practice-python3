#/usr/bin/env python3.6
# -*- coding:utf-8 -*-

__author__ = 'Jagger'


import math

'''
一个整数，它加上100后是一个完全平方数，再加上268又是一个完全平方数，请问该数是多少？ 
'''

def func():
	result = []
	for i in range (100000):
		x = int(math.sqrt(i + 100))
		y = int(math.sqrt(i + 268))

		if (x * x == i + 100) and (y * y == i + 268) :
			#print('x = %d, y = %d' % (x, y))
			result.append(i)

	return result



def func1():
	result = []
	for i in range(100000):
		x = math.sqrt(i + 100)
		y = math.sqrt(i + 268)

		if (x % 1 == 0) and (y % 1 == 0):			
			#print('x = %d, y = %d, i = %d' % (x, y, i))
			result.append(i)

	return result


print('result len %d' % len(func()))
print(func())

print('result len %d' % len(func1()))
print(func1())
