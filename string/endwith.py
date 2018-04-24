# coding=utf-8
import os
import stat

__author__ = 'hunter'

print os.listdir(".")

print [name for name in os.listdir(".") if name.endswith(('.py', 'sh'))]

print oct(os.stat('split.py').st_mode)

# 目的是查找可执行文件，并赋予可执行权限
os.chmod('split.py', os.stat('split.py').st_mode | stat.S_IXUSR)