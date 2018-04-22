from collections import namedtuple

__author__ = 'hunter'

Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])

s = Student('Jim', '16', 'male', '279@qq.com')

# s.age = 14

print s
