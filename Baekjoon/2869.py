'''


'''

import sys

a, b, v = map(int, sys.stdin.readline().split())
days = (v-b)//(a-b)
if (v-b)%(a-b) != 0:
    days += 1

print(days)
'''
while 1:
    days += 1
    v -= a
    if v <= 0:
        break
    v += b
'''
