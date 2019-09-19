# -*- coding: utf-8 -*-

#元组中的元素不允许修改和删除
tup1 = ("hello","world")
tup2 = (1,2,3)
print(tup1[1])
print(tup2[2])

#元组可以互相结合，也可以被整个删除
tup3 = tup1 + tup2
print(tup3)

del tup3
print(tup3)
#因为已经被删除，这一句会报错

