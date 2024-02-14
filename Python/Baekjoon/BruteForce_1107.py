# 리모컨

import sys
input = sys.stdin.readline

target = int(input().strip())
n = int(input())
disabled = list(map(int, input().split())) # 고장난 버튼

start = 100
mn = abs(100 - target) # + 또는 - 버튼으로만 채널을 이동하는 경우

if target == start:
    print(mn)
    exit()

lim = 1000001 # 50만 => 최대 한도를 50만*2+1로 설정
for num in range(lim):
    num = str(num)

    for j in range(len(num)):
        if int(num[j]) in disabled: break

        if j == len(num) - 1:
            mn = min(mn, abs(int(num) - target) + len(num))
print(mn)

