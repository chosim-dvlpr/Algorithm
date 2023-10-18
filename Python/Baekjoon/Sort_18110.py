# 아무 의견이 없다면 난이도 0
# 의견이 하나 이상 있다면, 난이도는 모든 사람의 난이도 의견의 30% 절사평균
# 절사평균 : 가장 큰, 작은 값 제외하고 평균 내는 것
# 30% 절사평균 : 위에서 15%, 아래서 15% 제외 후 평균 계산
# 제외되는 사람의 수 : 위, 아래에서 각각 반올림
# 25명 투표 => 4명씩 제외 (총 8명)
# 계산된 평균도 정수로 반올림됨

import sys

input = sys.stdin.readline

def merge_sort(lst):
  if len(lst) < 2:
    return lst

  mid = len(lst)//2
  left = merge_sort(lst[:mid])
  right = merge_sort(lst[mid:])

  return merge(left, right)

def merge(left, right):
  merged = []
  ll = rr = 0
  while ll < len(left) or rr < len(right):
    if ll < len(left) and rr < len(right):
      if left[ll] < right[rr]:
        merged.append(left[ll]) # 더 작은 것을 저장
        ll += 1
      else:
        merged.append(right[rr])
        rr += 1
    elif ll < len(left): # 오른쪽은 다 소진한 경우
      merged.append(left[ll])
      ll += 1
    elif rr < len(right): # 왼쪽은 다 소진한 경우
      merged.append(right[rr])
      rr += 1
  return merged

n = int(input()) # 난이도 의견의 개수
lst = []

for _ in range(n):
  lst.append(int(input()))

cut = round(n*0.15)
merged_list = merge_sort(lst)
merged_list = merged_list[cut:n-cut]
l = len(merged_list)
sums = sum(merged_list)

print(round(sums/l))


