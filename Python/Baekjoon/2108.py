import sys
from collections import Counter

n = int(sys.stdin.readline())
lst = []

for _ in range(n):
    a = int(sys.stdin.readline())
    lst.append(a)

lst.sort()

# 산술 평균
means = round(sum(lst) / n) # 산술평균 - int로 할 경우 올림이 되어 -1.8이 -1로 출력됨
                            # => round 사용하여 반올림

# 중앙값
median = lst[len(lst)//2]


# 최빈값
mode_list = Counter(lst).most_common(2)
# [(-2, 1), (1, 1)]
# (값, 등장횟수) 리스트로 2개까지 출력, 등장 횟수 많은 순서로 정렬됨
mode = mode_list[0][0]
if len(mode_list) > 1:
    if mode_list[0][1] == mode_list[1][1]:
        mode = mode_list[1][0]


# 범위 구하기
rng = lst[-1] - lst[0]



print(means)
print(median)
print(mode)
print(rng)