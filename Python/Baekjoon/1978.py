import sys
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
total = 0

for num in N_list:
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    if cnt == 2:
        total += 1 

print(total)