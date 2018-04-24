# coding: utf8
import re

__author__ = 'hunter'


def mySplit(s, ds):
    res = [s]
    for d in ds:
        t = []
        map(lambda x: t.extend(x.split(d)), res)
        res = t
    # 过滤空字符串
    return [x for x in res if x]


s = 'ab;cd|ef|his,,eng;ffg,w3rf'
print mySplit(s, ';|,')

# 方法二 正则表达式
print re.split(r'[;|,]+', s)
