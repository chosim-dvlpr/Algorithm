'''
n번째에 들어간 수를 출력하시오
순서는 항상 차례대로,
6이 연속으로 3번 들어감
666, 1666, 2666, 3666 . . .
10666, 11666, . . 16660~16669, 17666, . .

'''

import sys

n = int(sys.stdin.readline())
num = 666
lst = []

while 1:
    cnt = 0
    for i in range(len(str(num))-3+1):
        if str(num)[i:i+3] == '666':
            cnt += 1
    if cnt >= 1:
        lst.append(num)
    num += 1
    if len(lst) == n:
        print(lst[-1])
        break