# coding: utf8
from itertools import chain
from random import randint

__author__ = 'hunter'

chinese = [randint(60, 100) for _ in range(40)]
math = [randint(60, 100) for _ in range(40)]
english = [randint(60, 100) for _ in range(40)]

total = []

# zip生成的是元组的列表，属于并行操作
for c, m, e in zip(chinese, math, english):
    total.append(c + m + e)

print total

e1 = [randint(60, 100) for _ in range(40)]
e2 = [randint(60, 100) for _ in range(42)]
e3 = [randint(60, 100) for _ in range(42)]
e4 = [randint(60, 100) for _ in range(39)]

count = 0

for s in chain(e1, e2, e3, e4):
    if s > 90:
        count += 1

print count
