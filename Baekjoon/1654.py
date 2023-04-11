'''
k개의 랜선 ->모두 n개의 같은 길이의 랜선으로 만들기
만들 수 있는 최대 랜선의 길이는?

lans :이미 가지고 있는 각 랜선의 길이 리스트
'''


import sys

k, n = map(int, sys.stdin.readline().split())
lans = [int(sys.stdin.readline()) for _ in range(k)] # lans 길이 : k

start = 1
end = max(lans)

# 이분 탐색
while start <= end:
    mid = (start + end) // 2    # 길이를 이등분 하기 위해 중앙값을 mid에 저장
    cnt = 0                     # 랜선을 잘라 만들 수 있는 개수
    for i in range(k):
        cnt += lans[i] // mid   # 각 lan의 길이를 mid로 나눈 몫을 cnt에 더함
    if cnt >= n:                    # n보다 크거나 같다면
        start = mid + 1             # start 위치를 오른편으로 옮김
    else:                       # n보다 작다면
        end = mid - 1           # end 위치를 왼편으로 옮김

# 랜선의 길이가 가장 긴 경우를 출력해야 하므로 end 출력
print(end)


