# -*- coding: utf-8 -*-

#导入Python关键字包
import keyword

#这些关键字不能用作任何标识符名称
#print(keyword.kwlist)

#上一句输出的结果为list（列表），list可以修改
#可以添加元素，可以被索引和切片
kwl = keyword.kwlist
kwl[0] = "hello"
kwl.append("world")
kwl[1:-1] = []
print(kwl)

