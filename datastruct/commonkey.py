# coding=utf-8
from random import randint, sample

__author__ = 'hunter'

s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}

# 直接使用集合的交操作
print s1.viewkeys() & s2.viewkeys() & s3.viewkeys()

# 使用map和reduce

print reduce(lambda x, y: x & y, map(dict.viewkeys, [s1, s2, s3]))
