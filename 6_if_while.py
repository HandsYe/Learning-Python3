# -*- coding: utf-8 -*-

import random
#随机生成一个数
num = random.randint(0, 10)

#条件判断
if num == 0:
	print("This number is zero:", num)
elif num % 2 == 1:
	print("This number is odd:", num)
else:
	print("This number is even:", num)

total = 0
while num <= 10:
	num += 1
	total = total + num

print("total:", total)
