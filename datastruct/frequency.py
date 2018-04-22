# coding=utf-8
from collections import Counter

from random import randint

__author__ = 'hunter'

# 统计序列中的重复元素的频率，以及排序
data = [randint(0, 20) for _ in xrange(30)]

c = dict.fromkeys(data, 0)
# 这种方法可以得出每个元素的频率，若要进行排序，还要进行另外的操作
for x in data:
    c[x] += 1

c2 = Counter(data)

# 直接获取出现频率最高的元素
print c2.most_common(3)
