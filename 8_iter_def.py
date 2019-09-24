#-*- coding:utf-8 -*-

import sys
#可变参数列表,这些参数被包装进一个元组
def total(*args):
	sum = 0
	for i in args:
		sum += i
	return sum

print(total(32648923,1,3))


def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print (next(f), end="\n")
    except StopIteration:
        sys.exit()

