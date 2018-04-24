# coding=utf-8
__author__ = 'hunter'


class IntTuple(tuple):
    def __new__(cls, iterable):
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        # print g.next()
        return super(IntTuple, cls).__new__(cls, g)

    def __init__(self, iterable):
        # 这是生成的对象
        # print self
        # 初始化父类
        super(IntTuple, self).__init__(iterable)
        # pass


t = IntTuple([1, -1, 'abc', 6, ['x', 'y'], 3])
print t.__len__()
print t
