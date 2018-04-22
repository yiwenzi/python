# coding=utf-8
from random import randint

__author__ = 'hunter'

d = {x: randint(60, 100) for x in 'abcdefg'}

# 直接排序,是按key来排序的
print sorted(d)

# 使用zip函数，重新构造dict
d2 = sorted(zip(d.itervalues(), d.iterkeys()))
print d2

# 传入匿名函数，控制排序使用的值
d3 = sorted(d.items(), key=lambda x: x[1])
print d3
