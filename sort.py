#/usr/bin/env python3.6
# -*- coding:utf-8 -*-

__author__ = 'Jagger'


def func():
	arr = []
	num = int(input('please input num: \n'))
	
	for i in range(num):
		x = int(input('input digit:\n'))
		arr.append(x)

	print(arr)

	for i in range(len(arr) - 1):
		for j in range(len(arr) - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
			

	print(arr)


def func1():

	arr = []
	num = int(input('please input num:\n'))
	for i in range(num):
		x = int(input('input digit:\n'))
		arr.append(x)

	print(arr)
	arr.sort()
	print(arr)




func()
func1()
