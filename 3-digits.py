#/usr/bin/env python3.6
# -*- coding:utf-8 -*-

__author__ = 'Jagger'

'''
有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
'''


def func():
	r = []
	for i in range(1,5):
		for j in range(1,5):
			for k in range(1,5):
				if (i != j) and j != k and i != k:
					r += [i*100 + j*10 + k]
	return r


if __name__ == '__main__' :
	print("result: ")
	print(func())
