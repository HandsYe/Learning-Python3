#创建乘法表矩阵
import numpy as np
m = np.zeros(shape=(9,9))
for i in range(1,10):
	for ii in range(1,i+1):
		m[i-1][ii-1] = i*ii
		
print(m)

for i in range(1,10):
	for ii in range(1,i+1):
		print('{} * {} = {}|'.format(i,ii,i*ii),end = '')
	print()
