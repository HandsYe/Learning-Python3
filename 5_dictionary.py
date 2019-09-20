# -*- coding: utf-8 -*-

#字典是另一种可变容器模型，且可存储任意类型对象。
fruit = {"apple": "red", "banana": "yellow", "orange": "orange"}
print(fruit)
#修改键值
fruit["apple"] = "green"
#添加键值对
fruit["pineapple"] = "yellow"
#删除键值对
del fruit["banana"]

print(fruit)

#遍历字典中的键值对并输出
for key in fruit.keys():
	print(key + ":" + fruit[key] + "\n")

