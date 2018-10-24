#/usr/bin/evn python3.6
#-*-coding:utf-8-*-

__author__ = 'Jagger'

'''
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高 
于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提 
成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于 
40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于 
100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''



def func(profit):
	bonus = 0
	if profit <= 100000:
		bonus += profit * 0.1
	if profit > 100000 and profit <= 200000:
		bonus += (profit - 100000) * 0.075
	if profit > 200000 and profit <= 400000:
		bonus += (profit - 200000) * 0.05
	if profit > 400000 and profit <= 6000000:
		bonus += (profit - 400000) * 0.03
	if profit > 600000 and profit <= 1000000:
		bonus += (profit - 600000) * 0.015
	if profit > 1000000:
		bonus += (profit - 1000000) * 0.01

	return bonus


def func1(profit):
	bonus = 0
	bonus1 = 100000 * 0.1
	bonus2 = bonus1 + 100000 * 0.075
	bonus3 = bonus2 + 200000 * 0.05
	bonus4 = bonus3 + 200000 * 0.03
	bonus5 = bonus4 + 400000 * 0.015

	if profit <= 100000:
		bonus += profit * 0.1
	elif profit <= 200000:
		bonus = (profit - 100000) * 0.075 + bonus1
	elif profit <= 400000:
		bonus = (profit - 200000) * 0.05 + bonus2
	elif profit <= 600000:
		bonus = (profit - 400000) * 0.03 + bonus3
	elif profit <= 1000000:
		bonus = (profit - 600000) * 0.015 + bonus4
	else :
		bonus = (profit - 1000000) * 0.01 + bonus5

	return bonus

		
profit = int(input('input profit: \n'))
print(func1(profit))


	
