# coding=utf-8
from random import randint
__author__ = 'hunter'

# xrange在这里表示10次 randint每次只会生成一个
data = [randint(-10, 10) for _ in xrange(10)]
# data = [_ for _ in xrange(10)]
# data = [randint(-10, 10)]

result = filter(lambda x: x >= 0, data)

# 列表生成式的效率是filter的一倍
result2 = [x for x in data if x >= 0]

d = {x: randint(60, 100) for x in xrange(1, 21)}

d2 = {k: v for k, v in d.iteritems() if v > 90}

print d
print d2

s = set(data)

s2 = [x for x in s if x % 3 == 0]

s3 = {x for x in s if x % 3 == 0}

print s
print s2
print s3
