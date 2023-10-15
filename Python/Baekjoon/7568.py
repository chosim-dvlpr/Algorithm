'''
n : 전체 사람의 수

몸무게 : x
키 : y
덩치 : (x, y)
x, y가 둘 다 클 때 덩치가 큼
하나만 클 땐 비교할 수 없음
덩치 등수(k+1) : 자신보다 큰 덩치의 사람 수(k)로 결정
'''

n = int(input())
lst = []
for _ in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))

# Brute force (완전 탐색) - 전수검사
for i in lst:
    rank = 1
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]:
            # x, y 모두 큰 사람은 rank에 1씩 더하기
            rank += 1
    print(rank, end=' ')