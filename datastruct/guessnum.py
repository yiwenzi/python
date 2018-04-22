from collections import deque
from random import randint

__author__ = 'hunter'

N = randint(0, 100)
history = deque([], 5)


def guess(k):
    if k == N:
        print 'right'
        return True
    if k < N:
        print 'lower'
    if k > N:
        print 'greater'
    return False


while True:
    line = raw_input("Please enter a number: ")
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'history' or line == 'h?':
        print history
        print list(history)
