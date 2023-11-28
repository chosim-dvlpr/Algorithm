# 각 tc마다 0, 1이 출력되는 횟수 출력하기
# 0 : 1 0
# 1 : 0 1
# 2 : 1 1
# 3 : 1 2


import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n = int(input())
    f = []
    f.append((1, 0))    
    f.append((0, 1))
    if n > 1:
        for _ in range(2, n+1):
            f.append((f[-1][0] + f[-2][0], f[-1][1] + f[-2][1]))
        print(*f[n])
        continue
    elif n == 0:
        print(*f[0])
    else:
        print(*f[1])
        
