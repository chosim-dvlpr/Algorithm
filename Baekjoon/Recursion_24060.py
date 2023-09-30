import sys

# a : 배열의 크기
# k : 저장 횟수
# 배열 a에서 k번째 저장되는 수를 출력하기
# 저장횟수가 k보다 작으면 -1 출력
A, K = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
cnt = 0 # 저장 횟수
last = 0

# 병합정렬 - 분할 과정
def merge_sort(lst):
  if len(lst) == 1:
    return lst
  
  mid = len(lst) // 2 # 중앙값
  left = lst[:mid]    # 중앙값의 앞쪽까지
  right = lst[mid:]   # 중앙값부터 끝까지
  
  # 배열 길이가 1이 될 때까지 왼쪽, 오른쪽 나눔
  left = merge_sort(left)
  right = merge_sort(right)

  return merge(left, right)

# 병합정렬 - 병합 과정
def merge(left, right):
  global cnt, last

  if cnt == K:
    return last

  res = [] # 병합한 결과를 저장할 리스트
  i = j = 0

  # if left[-1] > right[-1]: # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우
  #   cnt += 1

  while len(left) > i or len(right) > j:
    if len(left) > i and len(right) > j:
      if left[i] <= right[j]: # 오른쪽이 더 클 때
        last = left[i]
        res.append(last)
        i += 1
      else:  # 왼쪽이 더 클 때
        last = right[j]
        res.append(last)
        j += 1
    elif len(left) > i: # 오른쪽을 다 소진한 경우 왼쪽만 저장
      last = left[i]      
      res.append(last)
      i +=1
    elif len(right) > j: # 왼쪽을 다 소진한 경우 오른쪽만 저장
      last = right[j]
      res.append(last)
      j += 1
    cnt += 1
  return res

result = merge_sort(a)
if cnt < K:
  result = -1
print(result)
