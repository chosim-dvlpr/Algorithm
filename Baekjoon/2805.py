'''
n : 나무의 수
m : 집으로 가져가려고 하는 나무의 길이
trees : 나무의 높이

나무를 자른 조각의 길이가 m보다 크거나 같아야 할 때,
땅으로부터 높이를 어떻게 설정해야 m에 가까워질 수 있을까?
(높이의 최댓값 구하기)

재귀 -> 시간 초과
=> 이분탐색
'''

import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
mx_height = 0   # 출력할 최대 높이

# 이분 탐색
trees.sort()
start = 0
end = max(trees)

while start <= end:
    height = (start + end) // 2
    sums = 0

    for tree in trees:
        if tree > height:
            sums += tree - height

    if sums >= m:
        if mx_height < height:
            mx_height = height
        start = height+1
    else:
        end = height-1

print(mx_height)

'''
# 시간 초과

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
height = 0
mn = 987654321
mn_height = 0
mx_tree = max(trees)
def cut_tree(trees, height):
    global mn, mn_height
    if mx_tree < height:     # 함수 종료 조건 - 가장 높은 나무보다 땅으로부터의 높이가 더 클때 종료
        return
    sums = 0
    for tree in trees:
        if tree > height:           # 자르려는 높이보다 나무가 더 크면 합계에 더함
            sums += tree - height
    if sums >= m:                   # sums가 원하는 길이보다 크거나 같을 때
        if mn > sums:               # sums가 새로운 최솟값일 때
            mn = sums               # 최솟값 갱신
            mn_height = height      # 최솟값일때의 높이 갱신
    cut_tree(trees, height + 1)  # 높이를 1씩 증가하며 반복
cut_tree(trees, height)
print(mn_height)
'''