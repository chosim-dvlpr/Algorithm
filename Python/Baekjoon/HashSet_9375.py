import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    m = int(input())
    clothes = {}
    for x in range(m):
        a, b = map(str, input().split())
        # key의 value 값은 상관 없고, 개수가 중요
        if clothes.get(b, -1) == -1: # 아직 key가 없을 때
            clothes[b] = 1
            continue
        clothes[b] += 1 # key가 있을 때

    total = 1
    for k in clothes.keys():
        total *= clothes[k]+1 # +1은 해당 항목의 옷을 입지 않은 경우

    # 모든 옷을 입지 않은 경우는 빼줌
    print(total-1)

